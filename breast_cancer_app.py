# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 11:29:21 2021

@author: LENOVO
"""

from flask import Flask, request, render_template
import pickle
from sklearn.preprocessing import StandardScaler




app=Flask(__name__)
model = pickle.load(open('breastcancer.pkl', 'rb'))


@app.route('/',methods=['GET'])
def Home():
    return render_template("breast_cancer.html")

standard_to = StandardScaler()
@app.route("/predict", methods=["GET", "POST"])
def predict():
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
        prediction=predict.model([[texture_mean, smoothness_mean, compactness_mean,concavity_mean, concave_points_mean, symmetry_mean, 
                                   compactness_se, concavity_se, concave_points_se, texture_worst, smoothness_worst, compactness_worst,
                                   concavity_worst, concave_points_worst,symmetry_worst,  fractal_dimension_worst]])
        
        if prediction ==1:
            return render_template("breast_cancer.html", prediction_text="Sorry! You have cancer")
        else:
            return render_template("breast_cancer.html", prediction_text="Congratulations! You are healthy")
    if __name__=="__main__":
        app.run(debug=True)
    
        
        
        
        
        
        
        
        
        