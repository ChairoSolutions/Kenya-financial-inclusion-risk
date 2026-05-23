# Kenya Financial Inclusion Risk Prediction

## Project Overview

This project focuses on analysing and predicting financial exclusion risk among Kenyan adults using the FinAccess 2021 Household Survey microdata.

Although Kenya is globally recognised for the success of mobile money services, a significant proportion of the population still lacks access to formal financial services such as:
- Banking services
- Insurance products
- SACCO services
- Pension schemes
- Regulated credit facilities

The project aims to:
- Identify individuals at risk of financial exclusion
- Understand the major factors contributing to exclusion
- Analyse exclusion patterns across demographic and geographic groups
- Develop predictive models for financial exclusion risk

---

# Problem Statement

Financial exclusion limits access to:
- Credit
- Savings
- Insurance
- Investment opportunities
- Economic growth opportunities

Understanding the drivers of financial exclusion can help:
- Financial institutions
- Policy makers
- Fintech companies
- Development organisations

design targeted interventions that improve financial inclusion across Kenya.

---

# Objectives

The main objectives of this project are to:

1. Explore and understand the FinAccess 2021 dataset
2. Identify key demographic and socioeconomic variables
3. Clean and preprocess the survey data
4. Create a financial exclusion target variable
5. Analyse financial inclusion patterns
6. Build predictive machine learning models
7. Evaluate model performance
8. Explain model predictions using explainable AI techniques
9. Develop a financial exclusion risk application

---

# Dataset Description

## Dataset Source
The project uses the:
- FinAccess 2021 Household Survey Microdata

Additional reference material:
- FinAccess 2024 Report
- FinAccess Dashboard

---

# Dataset Structure

The Excel workbook contains three major sheets:

| Sheet Name | Description |
|---|---|
| Dataset | Main survey responses |
| Variable Information | Variable descriptions and labels |
| Variable Values | Decoding for coded survey responses |

---

# Unit of Analysis

The unit of analysis is an individual survey respondent interviewed during the FinAccess 2021 survey.

---

# Key Variable Categories

The dataset contains variables related to:

## Demographic Information
- Age
- Gender
- Marital status
- Education level
- Household size

## Geographic Information
- County
- Region
- Rural or urban residence

## Socioeconomic Information
- Occupation
- Employment status
- Income level
- Asset ownership

## Financial Inclusion Indicators
- Banking usage
- Mobile money usage
- Savings behaviour
- Insurance access
- Credit access
- SACCO membership

---

# Data Exploration

The project includes exploratory analysis such as:
- Dataset structure inspection
- Variable dictionary creation
- Missing value analysis
- Duplicate row detection
- Feature type analysis
- Target balance analysis

---

# Target Variable

The project creates a binary target variable:

| Value | Meaning |
|---|---|
| 1 | Financially Excluded |
| 0 | Financially Included |

The target is derived using financial access indicators from the dataset.

---

# Target Leakage Considerations

Certain variables directly reveal financial inclusion status and may cause target leakage.

Examples include:
- Banking usage variables
- Mobile money usage variables
- Insurance usage variables
- Formal financial access indicators

These variables are excluded from predictive modelling where necessary.

---

# Machine Learning Models

The following machine learning models will be explored:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost

---

# Explainable AI

The project will use SHAP (SHapley Additive Explanations) to:
- explain model predictions,
- identify important variables,
- improve interpretability.

---

# Planned Outputs

The project aims to produce:
- Cleaned modelling dataset
- Exploratory analysis notebook
- Machine learning models
- Explainability visualisations
- County-level risk analysis
- Flask web application
- Dashboard visualisations

---

# Technologies Used

## Programming Language
- Python

## Libraries
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- xgboost
- shap
- openpyxl

---

# Project Workflow

1. Load dataset
2. Explore workbook sheets
3. Create variable dictionary
4. Decode survey values
5. Perform data quality checks
6. Create target variable
7. Clean and preprocess data
8. Perform exploratory data analysis
9. Train machine learning models
10. Evaluate models
11. Apply explainability techniques
12. Build deployment application

---

# Data Quality Checks

The following checks are performed:
- Missing values
- Duplicate rows
- Feature types
- Target balance

## Data Understanding

This project uses the **FinAccess 2021 Household Survey Microdata Excel Workbook** as the main dataset for exploring financial inclusion and exclusion among Kenyan adults. The notebook begins by inspecting the structure of the workbook, understanding available sheets, reviewing variable definitions, and identifying suitable variables for financial inclusion modelling.

### Dataset Source

The dataset is stored as an Excel
The primary modeling dataset is:

# Expected Impact

This project may help:
- identify financially vulnerable populations,
- support financial inclusion strategies,
- improve targeted interventions,
- guide policy and fintech innovation in Kenya.

---

# Author

Ainsley Nyambura Gichimu

---

# License

```text
1 = financially_excluded
0 = financially included
