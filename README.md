# Kenya Financial Inclusion Risk Prediction

Machine learning project using Kenya FinAccess 2021 survey data to predict, explain, and assess financial exclusion risk among Kenyan adults.


# Project Overview

Despite Kenya’s global recognition in mobile money innovation, a significant portion of the population still lacks access to formal financial services such as:
- Banking services
- Insurance products
- SACCO services
- Pension schemes
- Regulated credit facilities

This project uses the **FinAccess 2021 Household Survey Microdata** to:
- identify financially excluded individuals,
- understand drivers of exclusion,
- analyze vulnerable populations,
- and build predictive machine learning models for financial exclusion risk.

The project follows a complete end-to-end data science workflow:
- data understanding,
- preprocessing,
- exploratory analysis,
- machine learning,
- explainability,
- and Flask deployment.



# Problem Statement

Financial exclusion limits access to:
- credit,
- savings,
- insurance,
- investment opportunities,
- and broader economic participation.

Understanding the demographic and socioeconomic drivers of exclusion can help:
- policymakers,
- financial institutions,
- fintech companies,
- and development organizations

design targeted interventions that improve financial inclusion across Kenya.


# Project Objectives

The project aims to:

1. Explore and understand the FinAccess 2021 dataset
2. Create a financial exclusion target variable
3. Identify demographic and geographic patterns of exclusion
4. Build predictive machine learning models
5. Evaluate and compare model performance
6. Explain model predictions using explainable AI techniques
7. Compare project findings against the FinAccess 2024 report
8. Deploy the final model through a Flask application



# Dataset Information

## Dataset Source

The project uses:
- **FinAccess 2021 Household Survey Microdata**
- FinAccess 2024 Report (for comparative analysis)

Dataset source:
- Kenya National Bureau of Statistics (KNBS)
- FinAccess Household Survey



# Dataset Structure

The Excel workbook contains:

| Sheet Name | Description |
|---|---|
| Dataset | Main survey responses |
| Variable Information | Variable descriptions |
| Variable Values | Encoded value mappings |


# Unit of Analysis

The unit of analysis is an individual survey respondent interviewed during the FinAccess 2021 survey.


# Key Variables

The project explores variables related to:

## Demographic Information
- Age
- Gender
- Marital status
- Education level
- Household size

## Geographic Information
- County
- Region
- Rural/Urban residence

## Socioeconomic Information
- Occupation
- Employment status
- Income level
- Asset ownership

## Financial Inclusion Indicators
- Banking usage
- Mobile money usage
- Savings behavior
- Insurance access
- Credit access
- SACCO membership


# Project Workflow

The project follows the workflow below:

1. Data Understanding
2. Data Cleaning & Target Engineering
3. Exploratory Data Analysis (EDA)
4. Predictive Modeling
5. Explainability & Interpretability Analysis
6. Flask Deployment


# Repository Structure

```text
Kenya-financial-inclusion-risk/
│
├── app/
│   ├── app.py
│   └── templates/
│       └── index.html
│
├── artifacts/
│   └── metrics/
│
├── models/
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_cleaning_target_engineering.ipynb
│   ├── 03_exploratory_data_analysis.ipynb
│   ├── 04_predictive_modeling_evaluation.ipynb
│   ├── 05_model_explainability_2024_comparison.ipynb
│   └── 06_deployment_flask_app.ipynb
│
├── requirements.txt
└── README.md
```

# Data Preparation

The data preparation workflow transformed the raw FinAccess survey data into a leakage-controlled modeling dataset suitable for machine learning.

Key preprocessing steps included:
- Missing value assessment
- Target variable engineering
- Leakage variable removal
- Administrative column removal
- Feature engineering
- Feature type separation
- Class imbalance assessment
- Modeling dataset export

Additional interpretable variables were engineered to capture structural vulnerability patterns, including:
- Youth status
- Rural youth status
- Female-rural indicators


# Target Variable

A binary target variable was created:

| Value | Meaning |
|---|---|
| 1 | Financially Excluded |
| 0 | Financially Included |

The target variable was derived using financial access indicators from the dataset.


# Target Leakage Handling

Variables directly revealing financial inclusion status were excluded from modeling to prevent target leakage.

Examples include:
- Banking usage variables
- Mobile money variables
- Insurance usage indicators
- Formal financial access variables

Administrative identifiers and interview metadata were also removed.


# Exploratory Data Analysis

The EDA phase focused on understanding demographic and geographic exclusion patterns.

The analysis explored:
- County-level exclusion trends
- Gender patterns
- Rural vs Urban exclusion
- Education disparities
- Youth exclusion patterns
- Missing value analysis
- Cross-tabulation analysis

Visualizations were created to support interpretation and subgroup analysis.


# Machine Learning Approach

The project explored several classification models:

- Logistic Regression
- Random Forest
- Gradient Boosting
- Dummy Classifier (baseline)

The modeling workflow included:
- preprocessing pipelines,
- train-test splitting,
- SMOTE balancing,
- model comparison,
- and cross-validation.


# Model Evaluation

Models were evaluated using:
- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

Special attention was given to:
- Recall,
- False Negatives,
- and identifying vulnerable populations.


# Best Model

Gradient Boosting achieved the strongest overall performance based on:
- ROC-AUC,
- Recall,
- F1-score,
- and overall classification quality.

The model demonstrated strong discrimination ability in identifying financially excluded individuals.


# Explainability & Interpretability

The project applied explainable AI techniques to improve model transparency and interpretation.

Methods used:
- SHAP (SHapley Additive Explanations)
- Feature Importance Analysis
- Permutation Importance
- Mutual Information

The explainability analysis identified important drivers of exclusion risk, including:
- Education level
- Geographic inequality
- Rural residence
- Age-related vulnerability


# Comparative Analysis with FinAccess 2024

Project findings were compared against the FinAccess 2024 report to evaluate consistency in:
- exclusion trends,
- vulnerable populations,
- rural exclusion patterns,
- and demographic disparities.

This comparison strengthened the policy relevance of the project findings.


# Deployment

The final model was deployed locally using Flask.

The deployment workflow allows users to:
- submit demographic and socioeconomic information,
- generate financial exclusion risk predictions,
- receive exclusion probability scores,
- and view interpretable risk categories.



# Deployment Architecture

The deployment system includes:
- trained model serialization,
- saved preprocessing pipeline,
- Flask backend,
- HTML interface,
- and prediction API endpoints.


# Risk Classification Logic

| Probability Range | Risk Tier |
|---|---|
| Below 0.40 | Low Risk |
| 0.40 – 0.69 | Medium Risk |
| 0.70 and above | High Risk |


# Running the Project

## 1. Clone Repository

```bash
git clone <repository-url>
cd Kenya-financial-inclusion-risk
```


## 2. Install Dependencies

```bash
pip install -r requirements.txt
```



## 3. Launch Jupyter Notebook

```bash
jupyter notebook
```


## 4. Run Flask Application

```bash
python app/app.py
```

The application runs locally at:

```text
http://127.0.0.1:5000/
```


# Technologies Used

## Programming Language
- Python

## Libraries & Tools
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- xgboost
- shap
- Flask
- joblib
- openpyxl
- Git & GitHub


# Key Findings

The project identified several important financial exclusion patterns:
- Rural populations experience higher exclusion rates
- Geographic disparities exist across counties
- Education level strongly influences inclusion
- Youth populations show structural vulnerability
- Financial exclusion remains uneven across demographic groups


# Future Improvements

Potential future enhancements include:
- Hyperparameter optimization
- Dashboard integration
- Cloud deployment
- Additional feature engineering
- Advanced explainability workflows
- Real-time API deployment


# Expected Impact

This project may help:
- identify financially vulnerable populations,
- support financial inclusion strategies,
- improve targeted interventions,
- and guide policy and fintech innovation in Kenya.

# Contributors

- Ainsley Nyambura Gichimu
- Mercy Apondi Anyango
- Grace Waweru
- Frankline Kipkemboi
- Sylvia Kwamboka Mokindo
- Brian Chairo Mogire

# License

This project is intended for educational and research purposes.