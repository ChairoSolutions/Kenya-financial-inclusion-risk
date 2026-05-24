
from flask import Flask, request, jsonify, render_template
import joblib
import json
import pandas as pd
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "financial_exclusion_gradient_boosting_pipeline.joblib"
FEATURE_COLUMNS_PATH = BASE_DIR / "artifacts" / "metrics" / "04_feature_columns.json"

model = joblib.load(MODEL_PATH)

with open(FEATURE_COLUMNS_PATH, "r") as f:
    feature_columns = json.load(f)


def assign_risk_tier(exclusion_probability):
    if exclusion_probability < 0.40:
        return "Low Risk"
    elif exclusion_probability < 0.70:
        return "Medium Risk"
    else:
        return "High Risk"


def make_prediction(input_data):
    input_df = pd.DataFrame([input_data])

    # Add missing columns required by the trained pipeline
    for col in feature_columns:
        if col not in input_df.columns:
            input_df[col] = None

    # Keep exact column order used during training
    input_df = input_df[feature_columns]

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]
    risk_tier = assign_risk_tier(probability)

    result = {
        "prediction": int(prediction),
        "prediction_label": "Financially Excluded" if prediction == 1 else "Financially Included",
        "exclusion_probability": round(float(probability), 4),
        "exclusion_percentage": f"{probability * 100:.2f}%",
        "risk_tier": risk_tier
    }

    return result


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = request.get_json()
        result = make_prediction(input_data)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/predict_form", methods=["POST"])
def predict_form():
    try:
        input_data = {
            "gender": request.form.get("gender"),
            "settlement_type": request.form.get("settlement_type"),
            "education_level": request.form.get("education_level"),
            "employment_status": request.form.get("employment_status")
        }

        result = make_prediction(input_data)

        return render_template("index.html", result=result)

    except Exception as e:
        return render_template("index.html", error=str(e))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)