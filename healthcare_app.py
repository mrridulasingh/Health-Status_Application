# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 17:30:34 2021

@author: LENOVO
"""



import pickle


from flask import Flask, render_template, url_for, flash,redirect, request, send_from_directory


app=Flask(__name__)

model_heart=pickle.load(open("heart_d.pkl", "rb"))
model_breast_cancer=pickle.load(open("breastcancer.pkl", "rb"))
model_liver=pickle.load(open("liver_d.pkl", "rb"))

@app.route("/", methods=["GET"])
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/heartdisease", methods=["GET", "POST"])
def heartdisease():
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
        prediction=model_heart.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        if prediction ==1:
            return render_template('heartdisease.html', prediction_text='Sorry! You are suffering from heart disease', title="Heart Disease")
        else:
            return render_template('heartdisease.html', prediction_text='Congratulations! you are healthy', title= "Heart Disease")
    else:
        return render_template('heartdisease.html', title='Heart Disease')

@app.route("/breastcancerdisease", methods=["GET", "POST"])
def breastcancerdisease():
    if request.method == "POST":
        texture_mean= float(request.form['texture_mean']) 
        smoothness_mean=float(request.form['smoothness_mean'])
        compactness_mean=float(request.form['compactness_mean'])
        concavity_mean=float(request.form['concavity_mean'])
        concave_points_mean= float(request.form['concave points_mean'])
        symmetry_mean= float(request.form['symmetry_mean'])
        compactness_se=float(request.form['compactness_se'])
        concavity_se=float(request.form['concavity_se'])
        concave_points_se= float(request.form['concave points_se']) 
        texture_worst= float(request.form['texture_worst'])
        smoothness_worst=float(request.form['smoothness_worst'])
        compactness_worst=float(request.form['compactness_worst'])
        concavity_worst=float(request.form['concavity_worst'])
        concave_points_worst= float(request.form['concave points_worst'])
        symmetry_worst=float(request.form['symmetry_worst']) 
        fractal_dimension_worst=float(request.form['fractal_dimension_worst'])
        prediction=model_breast_cancer.predict([[texture_mean, smoothness_mean, compactness_mean,concavity_mean, concave_points_mean, symmetry_mean,
                                                 compactness_se, concavity_se, concave_points_se, texture_worst, smoothness_worst, compactness_worst, concavity_worst,
                                                 concave_points_worst,symmetry_worst,  fractal_dimension_worst]])
        
        if prediction ==1:
            return render_template("breast_cancer.html", prediction_text="Sorry! You have cancer", title="Breast Cancer")
        else:
            return render_template("breast_cancer.html", prediction_text="Congratulations! You are healthy", title="Breast Cancer")
    else:
        return render_template('breast_cancer.html',title='Breast Cancer')

@app.route("/liverdisease", methods=["GET", "POST"])
def liverdisease():
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
        prediction=model_liver.predict([[age,gender, total_bilirubin, direct_bilrubin, alkaline_phosphotase, alamine_aminotransferase, aspartate_aminotransferase,total_protein, albumin, albumin_globuline_ratio]])
        if prediction == 1:
            return render_template("liverdisease.html", prediction='Sorry!, You are suffering from liver related disease', title="Liver DIsease")
        else:
            return render_template("liverdisease.html", prediction="Congratulations! You are healthy", title="Liver DIsease")
    else:
        return render_template('liverdisease.html', title='Liver Disease')
    
if __name__=='__main__':
    app.run(debug=True)