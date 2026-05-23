# Kenya Financial Inclusion Risk Prediction

## Project Overview

This project focuses on financial inclusion in Kenya. Although Kenya is widely known for mobile money and digital financial innovation, some adults still remain excluded from formal and informal financial services such as banks, SACCOs, insurance, pensions, mobile banking, savings products, and regulated credit.

Our goal is to build a machine learning project that helps identify Kenyan adults who are most at risk of financial exclusion. The project will also explain the factors behind that risk, analyze county-level and subgroup patterns, compare 2021 findings with 2024 FinAccess trends, and deploy the final model through a Flask web application.

## Business Problem

Financial exclusion limits people’s ability to save, borrow, receive payments, manage emergencies, build businesses, and participate fully in the economy.

The main business question is:

**Can we predict which Kenyan adults are most at risk of financial exclusion, explain why they are at risk, and identify where exclusion is concentrated across counties and vulnerable groups?**

## Target Audience

The intended users of this project include:

- Banks
- Fintech companies
- SACCOs
- Microfinance institutions
- NGOs and development organizations
- Policymakers
- County governments
- Financial inclusion researchers

These users could apply the project insights to design better outreach strategies, improve financial products, and support underserved populations.

## Data Understanding

This project uses the **FinAccess 2021 Household Survey Microdata Excel Workbook** as the main dataset for exploring financial inclusion and exclusion among Kenyan adults. The notebook begins by inspecting the structure of the workbook, understanding available sheets, reviewing variable definitions, and identifying suitable variables for financial inclusion modelling.

### Dataset Source

The dataset is stored as an Excel
The primary modeling dataset is:

- **2021 FinAccess Household Survey Microdata**
  - Source: Kenya National Bureau of Statistics / FinAccess
  - Used for supervised machine learning and subgroup analysis

Supporting sources include:

- **2024 FinAccess Household Survey Report**
  - Used for trend comparison and current business context

- **FinAccess Dashboard**
  - Used for context, validation, and interpretation of national/county patterns

## Machine Learning Problem

This is a supervised machine learning classification problem.

The target variable will be:

```text
1 = financially_excluded
0 = financially included
# Model Deployment

## Deployment Overview

After completing data preparation, feature engineering, and model evaluation, the final stage of the project focused on deploying the machine learning model into a functional web application using Flask.

The purpose of deployment was to transform the trained model from a notebook-based solution into an interactive application capable of generating predictions from new user input in real time.

The deployed system allows users to:
- Submit financial and demographic information
- Process the input through the trained machine learning pipeline
- Generate financial inclusion risk predictions instantly
- Classify users into interpretable risk tiers

---

## Deployment Architecture

The deployment workflow consists of:

1. Loading the trained machine learning pipeline
2. Loading saved feature columns used during model training
3. Capturing user input through a Flask application
4. Converting the input into a structured dataframe
5. Passing the processed data into the trained model
6. Generating prediction probabilities
7. Assigning financial inclusion risk categories
8. Returning prediction results through the application interface

---

## Technologies Used

The deployment environment was built using:

- Python
- Flask
- Pandas
- Scikit-learn
- Joblib
- HTML/CSS

---

## Risk Classification Logic

The application assigns users into three financial inclusion risk categories based on predicted probabilities:

| Probability Range | Risk Tier |
|---|---|
| Below 0.40 | Low Risk |
| 0.40 – 0.69 | Medium Risk |
| 0.70 and above | High Risk |

This approach improves interpretability for stakeholders by translating prediction probabilities into understandable business categories.

---

## Running the Application Locally

To start the Flask application locally:

```bash
python app.py
```

The application runs on:

```bash
http://127.0.0.1:5000/
```

---

## Project Value

Deploying the model demonstrates how machine learning solutions can move beyond experimentation into practical business applications.

The deployed application provides:
- Faster prediction generation
- Improved accessibility for non-technical users
- Consistent financial inclusion risk assessment
- A foundation for future production-level deployment

This stage completes the end-to-end machine learning workflow by connecting data science development with real-world usability.