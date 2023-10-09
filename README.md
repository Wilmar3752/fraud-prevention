---
title: Fraud App - MELI
emoji: 🌍
colorFrom: green
colorTo: gray
sdk: gradio
sdk_version: 3.35.2
app_file: src/app.py
pinned: false
license: mit
---
# Modelo para deteccion de fraude 
Puedes encontrar la aplicación web haciendo click [AQUI](https://wilmars-fraud-meli-app.hf.space)

## Introducción
El fraude es un problema que afecta todo mercado en el que se realicen transacciones, MercadoLibre esta muy expuesta a este riesgo, por tanto, cualquier esfuerzo realizado para mitigarlo hace que se gane mucho dinero. En este caso propongo una metodología basada en Machine Learning que ayuda a encontrar la probabilidad de que una transacción sea fraudulenta y así tomar acciones en ella, ya sea rechazarla o no permitir el método de pago al cliente.

en la carpeta [notebooks](notebooks/) podremos encontrar un Analisis exploratorio de datos donde encuentro
todas las posibles transformaciones que se han de relizar sobre los datos, esto en el arhivo [eda.ipynb](notebooks/01-eda.ipynb)

### Feature engineering
Se realizaron una serie de transformaciones a la data, las cuales se detallan en el archivo [feature_engineering.ipynb](notebooks/02-feature_engineering.ipynb)
del cual obtenemos un pipeline como el que se muestra a continuacion [Imagen](img/pipeline.png)
