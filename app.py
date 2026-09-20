# -*- coding: utf-8 -*-
"""
Loan Default Prediction API
Author: Daniel O'Keeffe
Created: 21 September 2026

Description:
    This FastAPI application exposes a REST endpoint (/predict) that receives
    customer loan information and returns the predicted probability of 
    loan default using the trained Random Forest Model
    
Purpose:
    This script completes STEP 7 the Final Exam (Assignment).This API forms 
    the backend prediction service for the loan default assessment syetem. 
    It enables real time scoring of customer data  submitted from the 
    macro-enabled Excel workbook "BANK_LOAN_PREDICTIONS.xlsm"
"""

from fastapi import FastAPI 
from pydantic import BaseModel 
import pandas as pd 
import joblib 

# Create FastAPI App 
app = FastAPI() 

# Load trained model 
model = joblib.load("bankloan_rf_model.pkl") 

class Customer(BaseModel):
    AGE: int
    EMPLOY: int
    ADDRESS: int
    DEBTINC: float
    CREDDEBT: float
    OTHDEBT: float

@app.post("/predict")
def predict(customer: Customer):

    data = pd.DataFrame([{
        "AGE": customer.AGE,
        "EMPLOY": customer.EMPLOY,
        "ADDRESS": customer.ADDRESS,
        "DEBTINC": customer.DEBTINC,
        "CREDDEBT": customer.CREDDEBT,
        "OTHDEBT": customer.OTHDEBT
    }])

    probability = float(model.predict_proba(data)[0][1])
    classification = int(model.predict(data)[0])

    return {
        "Probability_Default": round(probability, 4),
        "Prediction": classification
    }