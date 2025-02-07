from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.metrics import confusion_matrix
import pandas as pd

class ScalerDf(BaseEstimator, TransformerMixin):

    def __init__(self, method):
        self.method = method

    def transform(self, X):
        X = pd.DataFrame(
            self.scaler.transform(X),
            columns=X.columns,
            index=X.index
        )
        return X

    def fit(self, X, y=None):
        if self.method == 'minmax':
            self.scaler = MinMaxScaler()
        elif self.method == 'standard':
            self.scaler = StandardScaler()
        elif self.method == 'none':
            return self
        else:
            raise ValueError("Invalid scaling method. Supported methods are 'minmax', 'standard', and 'none'.")

        self.scaler.fit(X)
        return self


def calcular_ganancia_total(matriz_confusion, valor_transaccion):
    """
    Calcula la ganancia total de la empresa dada la matriz de confusión y el valor de las transacciones.

    :param matriz_confusion: Matriz de confusión en forma de arreglo 2x2.
                             [ [TN, FP], 
                               [FN, TP] ]
    :param valor_transaccion: Valor de cada transacción (se asume igual para todas las transacciones).

    :return: Ganancia total de la empresa.
    """
    # Extraer valores de la matriz de confusión
    TN, FP = matriz_confusion[0]  # Primer fila: TN, FP
    FN, TP = matriz_confusion[1]  # Segunda fila: FN, TP

    # Ganancias y pérdidas basadas en las categorías de la matriz de confusión
    ganancia_TN = 0.25 * valor_transaccion  # Ganancia por transacción legítima correctamente identificada
    ganancia_TP = 0  # No hay ganancia por fraude detectado
    ganancia_FP = -0.25*valor_transaccion  # Pérdida por transacción legítima erróneamente clasificada como fraude
    ganancia_FN = -valor_transaccion  # Pérdida por fraude no detectado

    # Calcular la ganancia total
    ganancia_total = (TP * ganancia_TP) + (FP * ganancia_FP) + (TN * ganancia_TN) + (FN * ganancia_FN)

    return ganancia_total

def encontrar_umbral_optimo(model, X, y, umbrales, valor_transaccion):
    """
    Encuentra el umbral que maximiza las ganancias.

    :param model: Modelo entrenado de clasificación.
    :param X: Conjunto de características (datos de entrada).
    :param y: Etiquetas reales (verdaderas).
    :param umbrales: Lista de umbrales a probar.
    :param valor_transaccion: Valor de cada transacción (se asume igual para todas las transacciones).
    
    :return: El umbral que maximiza las ganancias.
    """
    max_ganancia = -float('inf')  # Inicializar la ganancia máxima
    umbral_optimo = None

    # Predecir probabilidades para cada transacción
    probabilidades = model.predict_proba(X)[:, 1]  # Probabilidades de la clase "fraude" (1)

    for umbral in umbrales:
        # Clasificar según el umbral
        y_pred = (probabilidades >= umbral).astype(int)

        # Obtener la matriz de confusión
        cm = confusion_matrix(y, y_pred)

        # Calcular la ganancia total para este umbral
        ganancia = calcular_ganancia_total(cm, valor_transaccion)

        # Actualizar el umbral óptimo si la ganancia es mayor
        if ganancia > max_ganancia:
            max_ganancia = ganancia
            umbral_optimo = umbral

    return umbral_optimo, max_ganancia
