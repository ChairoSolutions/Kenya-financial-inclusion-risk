import streamlit as st
import pandas as pd
import joblib
import json
from pathlib import Path

# -----------------------------
# Load model and feature columns
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "models" / "financial_exclusion_gradient_boosting_pipeline.joblib"
FEATURE_COLUMNS_PATH = BASE_DIR / "artifacts" / "metrics" / "04_feature_columns.json"

model = joblib.load(MODEL_PATH)

with open(FEATURE_COLUMNS_PATH, "r") as f:
    feature_columns = json.load(f)


# -----------------------------
# Helper function
# -----------------------------

def assign_risk_tier(prob):
    if prob < 0.40:
        return "Low Risk"
    elif prob < 0.70:
        return "Medium Risk"
    else:
        return "High Risk"


# -----------------------------
# App layout
# -----------------------------

st.set_page_config(
    page_title="Kenya Financial Exclusion Risk Predictor",
    layout="centered"
)

st.title("Kenya Financial Exclusion Risk Predictor")

st.write(
    "This app predicts whether an individual may be financially excluded "
    "based on demographic and socioeconomic inputs."
)

st.info(
    "The model uses 9 features: County, location type, gender, education level, "
    "marital status, adults, age, youth status, and rural-youth status."
)


# -----------------------------
# User input form
# -----------------------------

st.subheader("Enter Respondent Information")

County = st.selectbox(
    "County",
    [
        "Baringo",
        "Bomet",
        "Bungoma",
        "Busia",
        "Elgeyo-Marakwet",
        "Embu",
        "Garissa",
        "Homa Bay",
        "Isiolo",
        "Kajiado",
        "Kakamega",
        "Kericho",
        "Kiambu",
        "Kilifi",
        "Kirinyaga",
        "Kisii",
        "Kisumu",
        "Kitui",
        "Kwale",
        "Laikipia",
        "Lamu",
        "Machakos",
        "Makueni",
        "Mandera",
        "Marsabit",
        "Meru",
        "Migori",
        "Mombasa",
        "Murang'a",
        "Nairobi",
        "Nakuru",
        "Nandi",
        "Narok",
        "Nyamira",
        "Nyandarua",
        "Nyeri",
        "Samburu",
        "Siaya",
        "Taita Taveta",
        "Tana River",
        "Tharaka-Nithi",
        "Trans Nzoia",
        "Turkana",
        "Uasin Gishu",
        "Vihiga",
        "Wajir",
        "West Pokot"
    ]
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

education_level = st.selectbox(
    "Education Level",
    ["No education", "Primary", "Secondary", "Tertiary"]
)

marital_status = st.selectbox(
    "Marital Status",
    ["Single", "Married", "Divorced/Separated", "Widowed"]
)

adults = st.number_input(
    "Number of Adults in Household",
    min_value=1,
    max_value=20,
    value=2,
    step=1
)

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30,
    step=1
)

is_youth = 1 if age <= 35 else 0
is_rural_youth = 1 if location_type == "Rural" and is_youth == 1 else 0

st.write(f"Auto-calculated youth status: **{is_youth}**")
st.write(f"Auto-calculated rural-youth status: **{is_rural_youth}**")


# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Financial Exclusion Risk"):

    input_data = {
        "County": County,
        "location_type": location_type,
        "gender": gender,
        "education_level": education_level,
        "marital_status": marital_status,
        "adults": adults,
        "age": age,
        "is_youth": is_youth,
        "is_rural_youth": is_rural_youth
    }

    input_df = pd.DataFrame([input_data])

    # Ensure exact training column order
    input_df = input_df[feature_columns]

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]
    risk_tier = assign_risk_tier(probability)

    st.subheader("Prediction Result")

    st.metric(
        "Prediction",
        "Financially Excluded" if prediction == 1 else "Financially Included"
    )

    st.metric(
        "Exclusion Probability",
        f"{probability * 100:.2f}%"
    )

    st.metric(
        "Risk Tier",
        risk_tier
    )

    st.write("Input sent to model:")
    st.dataframe(input_df)