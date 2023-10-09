import gradio as gr
import pandas as pd
import joblib
import numpy as np
import json

data = pd.read_csv('data/MercadoLibre Data Scientist Technical Challenge - Dataset.csv')
pipeline = joblib.load('models/final_pipeline.joblib')
ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o','p', 'fecha', 'monto', 'score']
data = data[ls]
def sentence_builder(a, b, c, d, e, f, g, h, j, k, l, m, n, o, p, fecha, monto, score):
    
    ls = [a, b, c, d, e, f, g, h, j, k, l, m, n, o, p, fecha, monto, score]
    df = pd.DataFrame(ls).T
    
    df.columns = data.columns
    df['a'] = df['a'].astype('int64')
    df['b'] = df['b'].astype('float64')
    df['c'] = df['c'].astype('float64')
    df['d'] = df['d'].astype('float64')
    df['e'] = df['e'].astype('float64')
    df['f'] = df['f'].astype('float64')
    df['g'] = df['g'].astype('object')
    df['h'] = df['h'].astype('int64')
    df['j'] = df['j'].astype('object')
    df['k'] = df['k'].astype('float64')
    df['l'] = df['l'].astype('float64')
    df['m'] = df['m'].astype('float64')
    df['n'] = df['n'].astype('int64')
    df['o'] = df['o'].astype('object')
    df['p'] = df['p'].astype('object')
    df['fecha'] = df['fecha'].astype('object')
    df['monto'] = df['monto'].astype('float64')
    df['score'] = df['score'].astype('int64')
    predict_proba = pipeline.predict_proba(df)[:, 1]
    predict = np.where(predict_proba<0.05018921, 'No fraude', 'Fraude')
    print(predict)
    output = {'probability':str(predict_proba[0]),
              'prediction':predict[0]}
    print(output)
    return json.dumps(output)


demo = gr.Interface(
    fn = sentence_builder,
    inputs=[
        gr.Number(value=4, label="a"), 
        gr.Number(value=0.5217, label="b"), 
        gr.Number(value=17889.0, label="c"), 
        gr.Number(value=1.0, label="d"), 
        gr.Number(value=0.2830350998, label="e"), 
        gr.Number(value=12.0, label="f"), 
        gr.Textbox(value="BR", label="g"), 
        gr.Number(value=36, label="h"), 
        gr.Textbox(value="cat_4744ece", label="j"), 
        gr.Number(value=0.6366103624, label="k"), 
        gr.Number(value=2470.0, label="l"), 
        gr.Number(value=308.0, label="m"), 
        gr.Number(value=1, label="n"), 
        gr.Textbox(value='Y', label="o"), 
        gr.Textbox(value="Y", label="p"), 
        gr.Textbox(value="2020-03-18 09:31:52", label="fecha"), 
        gr.Number(value=24.89, label="monto"), 
        gr.Number(value=93, label="score")
        ], 
        outputs="json"
        )

if __name__ == "__main__":
    demo.launch()