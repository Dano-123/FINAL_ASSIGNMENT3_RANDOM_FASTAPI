
## **Final Exam (Assignment) - Productionization of Machine Learning Systems Overview**

This project implements a machine learning system to predict the probability that a customer will default on a loan. The system includes:

- A Random Forest classification model trained on the BankLoan dataset.
- A FastAPI endpoint (`/predict`) that returns the predicted probability of default.
- A macro-enabled Excel workbook (.xlsm) with a Submit button that sends customer data to the API and displays the prediction.

---

## 1. Training the Model

The model is trained using:

- Features: AGE, EMPLOY, ADDRESS, DEBTINC, CREDDEBT, OTHDEBT  
- Target: DEFAULTER  
- Algorithm: RandomForestClassifier with 500 trees

The trained model is saved as:

```
bankloan_rf_model.pkl
```

---

## 2. FastAPI Endpoint

The API exposes a single POST endpoint:

```
POST /predict
```

### Request JSON format:

```json
{
  "AGE": 2,
  "EMPLOY": 9,
  "ADDRESS": 4,
  "DEBTINC": 13.8,
  "CREDDEBT": 1.35,
  "OTHDEBT": 2.65
}
```

### Response format:

```json
{
  "Probability_Default": 0.122,
  "Prediction": 1
}
```

---

## 3. Excel Integration

A macro-enabled Excel workbook (`Bankloan_Predictions.xlsm`) contains:

- A Submit button  
- VBA code that sends customer data to the FastAPI endpoint  
- The predicted probability is displayed in the sheet  

This satisfies assignment Step 8.

---

## 4. Running the API

Start the FastAPI server using:

```
uvicorn app:app --reload
```

Ensure `bankloan_rf_model.pkl` is in the same directory.

---

## 5. Requirements

The project dependencies are listed in `requirements.txt`:

```
fastapi
uvicorn
pydantic
pandas
scikit-learn
joblib
openpyxl
```

---

## 6. Files to Submit

Submit:

- `Training script (train_model.py)`
- `Testing script (predict_file.py)`
- `FastAPI application (app.py)`
- `Trained model file (bankloan_rf_model.pkl)`
- `Training dataset (BANK LOAN.xlsx)`
- `Test dataset (BANK_LOAN_TEST.xlsx)`
- `Prediction output workbook (Bankloan_Predictions.xlsx)`
- `Macro enabled Excel interface (BANK_LOAN_PREDICTIONS.xlsm)`
- `Requirements file (requirements.txt)`
- `README documentation`
- `URL link for API (Link- Final Assignment.txt)`
---
