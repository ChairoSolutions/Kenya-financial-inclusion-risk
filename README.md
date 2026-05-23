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


## Financial Exclusion Classification Model
##### Objective

We aim to predict whether an individual is financially excluded (yes/no) using classification models:

* Logistic Regression
* Random Forest
* Gradient Boosting

We will:

* Build ML pipelines
* Train models
* Compare performance
* Evaluate using Accuracy, Precision, Recall, ROC-AUC
* Analyze confusion matrix (FP, FN)
* Recommend best model

## Tools
- Python
- Pandas
- Scikit-learn
- Matplotlib
# Target Variable Distribution
We analyze the distribution of the target variable to check class imbalance.
# Splitting Features and Target Variable
We separate the dataset into:
- X: input features
- y: target variable (financial exclusion)
# Identifying Feature Types
We separate columns into:
- Categorical features (need encoding)
- Numerical features (can be scaled if needed)
# Train-Test Split

We split the dataset BEFORE preprocessing to avoid data leakage.

The test set must remain completely unseen during training.

We split data into:
- Training set (80%)
- Testing set (20%)

Stratification preserves the target distribution in both sets.
# Data Preprocessing Pipeline

We build preprocessing pipelines for:

## Categorical Columns
- Missing value imputation using most frequent value
- OneHotEncoding

## Numerical Columns
- Missing value imputation using median
- Standard scaling

ColumnTransformer allows different preprocessing for different column types.
# Handling Class Imbalance with SMOTE

SMOTE (Synthetic Minority Oversampling Technique) creates synthetic examples of the minority class.

Benefits:
- reduces class imbalance
- improves recall for minority class
- helps models learn minority patterns better

SMOTE is applied ONLY on training data to avoid data leakage.
# Model Building

We define three classification models:
1. Dummy Classifier
2. Logistic Regression → baseline interpretable model
3. Random Forest → ensemble tree-based model
4. Gradient Boosting → advanced boosting model

Each model is wrapped in a pipeline with preprocessing.
# Baseline Model: Dummy Classifier

The Dummy Classifier predicts using simple rules without learning patterns.

Purpose:
- establish baseline performance
- compare whether advanced models truly improve performance

If advanced models do not outperform Dummy Classifier, the models are not useful.
#  Model Performance Comparison

We compare all classification models using key evaluation metrics:

- Accuracy → overall correctness
- Recall → ability to detect financially excluded individuals
- F1 Score → balance between precision and recall
- ROC-AUC → ability to distinguish between classes

The Dummy Classifier serves as the baseline model.
#  Model Comparison Interpretation

###  Dummy Classifier
Serves as the baseline model and represents minimal predictive capability.

###  Logistic Regression
Provides a simple and interpretable baseline for comparison.

###  Random Forest
Improves performance by capturing non-linear relationships using multiple decision trees.

###  Gradient Boosting
Achieved the strongest overall performance, especially in ROC-AUC and Recall, making it the most suitable model for predicting financial exclusion.

###  Final Recommendation
Gradient Boosting is selected as the final model because:
- It achieved the highest predictive performance
- It balances recall and overall classification quality
- It reliably identifies financially excluded individuals
# Final Model Comparison

We compare all models using key evaluation metrics and select the best performing model based on ROC-AUC and Recall (important for identifying vulnerable individuals).
# Best Model: Gradient Boosting

After comparing all models (Dummy, Logistic Regression, Random Forest, and Gradient Boosting), the Gradient Boosting model performed best based on evaluation metrics
# Confusion Matrix - Gradient Boosting

The confusion matrix helps us understand how well the model is performing on unseen data.

It shows:
- True Positives (TP): correctly predicted financially excluded individuals
- True Negatives (TN): correctly predicted non-excluded individuals
- False Positives (FP): wrongly predicted as excluded
- False Negatives (FN): missed excluded individuals (critical error in this project)
# Recommendations for Improvement
To reduce False Negatives and improve Recall:

- tune classification threshold
- optimize Gradient Boosting hyperparameters
- test XGBoost or LightGBM
- engineer stronger socioeconomic features
- experiment with class weighting
- further refine SMOTE strategy

# Final Conclusion

The Gradient Boosting model demonstrates strong overall discrimination ability and stable performance, but the confusion matrix shows that identifying financially excluded individuals remains challenging.

The model is highly reliable for identifying financially included individuals, but additional optimization is needed to improve detection of vulnerable populations and reduce False Negatives.
#  Cross Validation - Gradient Boosting
Cross-validation evaluates model stability across multiple data splits.

Benefits:
- reduces overfitting risk
- provides more reliable performance estimate
- measures generalization ability

We use ROC-AUC as the evaluation metric.
#  Final Conclusion 
## Best Model: Gradient Boosting

Gradient Boosting achieved the best balance of:
- ROC-AUC
- Recall
- F1-score
- Generalization performance

## Why Gradient Boosting Performed Best
- captures non-linear relationships
- sequentially corrects weak learner errors
- handles complex feature interactions

## Business Impact
The model can help identify financially excluded individuals more accurately, supporting:
- targeted interventions
- financial inclusion policies
- resource allocation strategies

## Key Recommendation
Future improvements may include:
- hyperparameter tuning
- SHAP explainability
- feature engineering
- deployment using Streamlit or FastAPI
```

## Data Preparation

The data preparation process transformed the raw 2021 FinAccess household survey dataset into a clean, leakage-controlled modeling dataset suitable for exploratory analysis and machine learning. The workflow began by reloading the raw survey data independently to ensure notebook reproducibility.

A binary target variable, `financially_excluded`, was engineered from the `excluded_informal_banked2022` column, where respondents classified as “Excluded” were mapped to 1 and those categorized as “Banked” or “Other Formal” were mapped to 0. To reduce target leakage, variables directly related to financial access, including banking usage, mobile money, loans, savings, SACCO participation, insurance, and other formal or informal financial service indicators, were identified and excluded from the structural-risk modeling dataset.
 
Administrative and identifier-related columns such as interview IDs and household identifiers were also removed to prevent overfitting. A small set of safe demographic and socioeconomic predictors was then selected, including county, rural/urban status, gender, age, education level, marital status, and household composition. 
  
Additional interpretable features such as youth status, rural youth status, and female-rural indicators were engineered to capture structural vulnerability patterns associated with financial exclusion.
  
Missing values were assessed and found to be negligible within the selected modeling variables, while class imbalance in the target variable was validated and visualized for downstream modeling awareness.
   
The dataset was further cleaned by restricting the modeling population to respondents aged 18–100 years to improve deployment realism and demographic consistency. Finally, cleaned datasets, feature metadata, leakage review artifacts, feature-type definitions, and reproducibility files were exported for downstream exploratory analysis and machine learning workflows.

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
