# -*- coding: utf-8 -*-
"""
Loan Default Prediction: Model Training Script
Author: Daniel O'Keeffe
Created: 20 September 2026

Description:
    This script trains, evaluates, and saves a Random Forest classification
    model for predicting loan default using the "BANK LOAN.csv" dataset.
    
Purpose:
    This script forms the core machine learning component of the loan default
    prediction system, enabling deployment-ready model generation.
"""

import pandas as pd 
import joblib   
from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix 

# Load dataset file
df = pd.read_csv ("BANK LOAN.csv")

# Separate predictors (X) and target (y)
X = df.drop(["SN", "DEFAULTER"], axis = 1)                       
y = df["DEFAULTER"]  

# Split into Train & Test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# Building RANDOM FOREST Model 
rf_model = RandomForestClassifier(            
    n_estimators=500,                     
    random_state=42,
    n_jobs=-1
)                           

# Fit RANDOM FOREST Model on X_train & y_train training data
rf_model.fit(X_train, y_train)

# Predict probabilities on test data
y_pred  = rf_model.predict(X_test)

print("Accuracy:") 
print(accuracy_score(y_test, y_pred)) 
      
print("\nConfusion Matrix:") 
print(confusion_matrix(y_test, y_pred)) 
     
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save trained model
joblib.dump(rf_model,"bankloan_rf_model.pkl")
print("Model saved succuessfully") 