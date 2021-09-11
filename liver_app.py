# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 22:26:43 2021

@author: LENOVO
"""

from flask import Flask, request, render_template
import pickle



app=Flask(__name__)
model=pickle.load(open("liver_d.pkl", 'rb'))

@app.route("/")
def home():
    return render_template("liverdisease.html")

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        age=int(request.form['Age'])
        gender=int(request.form["Gender"])
        total_bilirubin=float(request.form['Total_Bilirubin'])
        direct_bilrubin=float(request.form['Direct_Bilirubin'])
        alkaline_phosphotase=int(request.form['Alkaline_Phosphotase'])
        alamine_aminotransferase= int(request.form['Alamine_Aminotransferase'])
        aspartate_aminotransferase = int(request.form['Aspartate_Aminotransferase'])
        total_protein=float(request.form['Total_Protiens'])
        albumin= float(request.form['Albumin'])
        albumin_globuline_ratio= float(request.form['Albumin_and_Globulin_Ratio'])
        prediction=predict.model([[age, gender, total_bilirubin, direct_bilrubin, alkaline_phosphotase, alamine_aminotransferase, aspartate_aminotransferase,total_protein, albumin, albumin_globuline_ratio]])
        if prediction == 1:
            return render_template("liverdisease.html", prediction='Sorry!, You are suffering from liver related disease')
        else:
            return render_template("liverdisease.html", prediction="Congratulations! You are healthy")
    if __name__== "__main__":
        app.run(debug=True)