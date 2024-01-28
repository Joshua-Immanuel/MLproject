from flask import Flask, request, render_template
import numpy as np 
import pandas as pd 
from src.pipeline.predict_pipeline import CustomData,PredictPieline

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predcit',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
        request.form.get('gender'),
        request.form.get('ethnicity'),
        request.form.get('parental_level_of_education'),
        request.form.get('lunch'),
        request.form.get('test_preparation_course'),
        float(request.form.get('writing_score')),
        float(request.form.get('reading_score'))
        )
        df=data.get_predict_df()
        print(df)
        predict_pipeline=PredictPieline()
        results=predict_pipeline.predict(df)
        return render_template('home.html',results=results)
    

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port=7100)