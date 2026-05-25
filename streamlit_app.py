import streamlit as st
import pandas as pd
import joblib
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "models" / "financial_exclusion_gradient_boosting_pipeline.joblib"
FEATURE_COLUMNS_PATH = BASE_DIR / "artifacts" / "metrics" / "04_feature_columns.json"

model = joblib.load(MODEL_PATH)

with open(FEATURE_COLUMNS_PATH, "r") as f:
    feature_columns = json.load(f)

def assign_risk_tier(prob):
    if prob < 0.40:
        return "Low Risk"
    elif prob < 0.70:
        return "Medium Risk"
    else:
        return "High Risk"

st.title("Kenya Financial Exclusion Risk Predictor")

st.write(
    "This app predicts whether an individual may be financially excluded "
    "based on demographic and socioeconomic inputs."
)

gender = st.selectbox("Gender", ["Male", "Female"])
settlement_type = st.selectbox("Settlement Type", ["Urban", "Rural"])
education_level = st.selectbox("Education Level", ["Primary", "Secondary", "Tertiary"])
employment_status = st.selectbox("Employment Status", ["Employed", "Unemployed"])

if st.button("Predict Financial Exclusion Risk"):

    input_data = {
        "gender": gender,
        "settlement_type": settlement_type,
        "education_level": education_level,
        "employment_status": employment_status
    }

    input_df = pd.DataFrame([input_data])

    for col in feature_columns:
        if col not in input_df.columns:
            input_df[col] = None

    input_df = input_df[feature_columns]

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]
    risk_tier = assign_risk_tier(probability)

    st.subheader("Prediction Result")

    st.write("Prediction:", "Financially Excluded" if prediction == 1 else "Financially Included")
    st.write("Exclusion Probability:", f"{probability * 100:.2f}%")
    st.write("Risk Tier:", risk_tier)