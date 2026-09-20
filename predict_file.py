# -*- coding: utf-8 -*-
"""
Loan Default Prediction: Test Data Scoring Script
Author: Daniel O'Keeffe
Created: 20 September 2026

Description:
    This script loads a previously trained Random Forest model and applies
    it to the BANK LOAN_TEST.csv dataset to estimate the probability of loan
    default for each customer application.
    
Purpose:
    This script completes Step 5 of the Final Exam (Assignment) by producing
    default probability estimates for the test dataset. All default probability
    estimates are stored in an Excel workbook named "Bankloan_Predictions.xlsx"
    for later evaluation.
"""

import pandas as pd 
import joblib
   
# Load trained model 
model = joblib.load("bankloan_rf_model.pkl") 

# Load dataset file
df = pd.read_csv ("BANK LOAN_TEST.csv")

# Prepare predictors X
X = df.drop(["SN", "DEFAULTER"], axis = 1)    

# Predict default probability 
probabilities = model.predict_proba(X)[:, 1] 

# Round probabilites to 4 decimal places
probabilities_rounded = probabilities.round(4)

# Add probability column 
df["Probability_Default"] = probabilities 

# Save results 
df.to_excel("Bankloan_Predictions.xlsx", index=False)

print("Predictions successfully exported.")

