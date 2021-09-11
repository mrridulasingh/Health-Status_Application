# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, request, render_template
import sklearn
import pickle
import pandas as pd

app=Flask(__name__)
model=pickle.load(open("heart_d.pkl", 'rb'))


@app.route("/")
def home():
    return render_template("heartdisease.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        age=int(request.form["age"])
        sex=int(request.form['sex'])       
        cp=int(request.form['cp'])
        trestbps=int(request.form['trestbps'])
        chol=int(request.form['chol'])
        fbs=int(request.form['fbs'])
        restecg=int(request.form['restecg'])
        thalach=int(request.form['thalach'])
        exang=int(request.form['exang'])
        oldpeak=float(request.form['oldpeak'])
        slope=int(request.form['slope'])
        ca=int(request.form['ca'])
        thal=int(request.form['thal'])
        prediction=model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        if prediction ==1:
            return render_template('heartdisease.html', prediction_text='Sorry! You are suffering from heart disease')
        else:
            return render_template('heartdisease.html', prediction_text='Congratulations! you are healthy')
    if __name__=="__main__":
        app.run(debug=True)
        