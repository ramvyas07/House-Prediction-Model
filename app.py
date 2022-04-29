from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import keras #to build a neural network model that predicts the price of a house.

import pandas as pd #to read data
import numpy as np
from sklearn.preprocessing import StandardScaler
import tensorflow
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model_y_4.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        bedrooms = int(request.form['bedrooms'])
        bathrooms = float(request.form['Bathrooms'])
        sqft_living = int(request.form['sqft_living'])
        sqft_lot = int(request.form['sqft_lot'])
        waterfront = int(request.form['waterfront'])
        view = int(request.form['view'])
        condition = int(request.form['cond'])
        yr_built = int(request.form['built'])
        statezip = int(request.form['zipcode'])
        floors = float(request.form['floors'])
        no_year = 2022 - yr_built

        # Year = int(request.form['Year'])
        # Present_Price=float(request.form['Present_Price'])
        # Kms_Driven=int(request.form['Kms_Driven'])
        # Kms_Driven2=np.log(Kms_Driven)
        # Owner=int(request.form['Owner'])
        # Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
        # if(Fuel_Type_Petrol=='Petrol'):
        #         Fuel_Type_Petrol=1
        #         Fuel_Type_Diesel=0
        # else:
        #     Fuel_Type_Petrol=0
        #     Fuel_Type_Diesel=1
        # Year=2020-Year
        # Seller_Type_Individual=request.form['Seller_Type_Individual']
        # if(Seller_Type_Individual=='Individual'):
        #     Seller_Type_Individual=1
        # else:
        #     Seller_Type_Individual=0	
        # Transmission_Mannual=request.form['Transmission_Mannual']
        # if(Transmission_Mannual=='Mannual'):
        #     Transmission_Mannual=1
        # else:
        #     Transmission_Mannual=0
        prediction=model.predict([[bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, statezip,no_year]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="No Price")
        else:
            return render_template('index.html',prediction_text="Your current price home is {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

