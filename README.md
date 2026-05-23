# Explainability & Interpretability Analysis
# Kenya Financial Inclusion Risk Prediction

## Overview

Following the model training and evaluation stages, this phase focused on explainability and interpretability analysis for financial exclusion prediction in Kenya.

The objective was to understand how the trained Gradient Boosting model makes predictions and identify the key drivers of financial exclusion risk.

The analysis applied:
- SHAP (SHapley Additive Explanations)
- Permutation Importance
- Mutual Information
- Feature Importance Analysis

These methods improved model transparency and connected predictions to real-world financial inclusion challenges.


## Key Findings

The explainability analysis identified important predictors of financial exclusion risk, including:
- Education level
- Age
- County
- Rural location

SHAP analysis showed that geographic inequality and lower education levels were strongly associated with higher exclusion risk.

Permutation Importance and Mutual Information analysis confirmed the importance of demographic and geographic variables in prediction performance.


## Why Explainability Matters

Explainability helps users understand:
- Why predictions were made
- Which features influenced outcomes
- Whether the model is fair and reliable
## Data Understanding

This project uses the **FinAccess 2021 Household Survey Microdata Excel Workbook** as the main dataset for exploring financial inclusion and exclusion among Kenyan adults. The notebook begins by inspecting the structure of the workbook, understanding available sheets, reviewing variable definitions, and identifying suitable variables for financial inclusion modelling.

### Dataset Source

The dataset is stored as an Excel
The primary modeling dataset is:

This improves transparency, trust and decision-making in financial inclusion systems.


## Business & Policy Insights

The findings suggest that financial exclusion in Kenya is influenced by structural and socio-economic barriers.

The insights generated from this analysis can support:
- Financial literacy programs
- Rural banking expansion
- Digital financial inclusion initiatives
- Youth-focused financial services


## Contribution

This phase contributed:
- SHAP explainability analysis
- Feature importance evaluation
- Business interpretation of model findings
- Exported explainability outputs for reporting and future Flask integration


## Conclusion

This stage transformed the machine learning model into a more transparent and explainable financial inclusion tool by connecting predictions to meaningful real-world insights.
```text
1 = financially_excluded
0 = financially included

```

## Data Preparation

The data preparation process transformed the raw 2021 FinAccess household survey dataset into a clean, leakage-controlled modeling dataset suitable for exploratory analysis and machine learning. The workflow began by reloading the raw survey data independently to ensure notebook reproducibility.

A binary target variable, `financially_excluded`, was engineered from the `excluded_informal_banked2022` column, where respondents classified as “Excluded” were mapped to 1 and those categorized as “Banked” or “Other Formal” were mapped to 0. To reduce target leakage, variables directly related to financial access, including banking usage, mobile money, loans, savings, SACCO participation, insurance, and other formal or informal financial service indicators, were identified and excluded from the structural-risk modeling dataset.
 
Administrative and identifier-related columns such as interview IDs and household identifiers were also removed to prevent overfitting. A small set of safe demographic and socioeconomic predictors was then selected, including county, rural/urban status, gender, age, education level, marital status, and household composition. 
  
Additional interpretable features such as youth status, rural youth status, and female-rural indicators were engineered to capture structural vulnerability patterns associated with financial exclusion.
  
Missing values were assessed and found to be negligible within the selected modeling variables, while class imbalance in the target variable was validated and visualized for downstream modeling awareness.
   
The dataset was further cleaned by restricting the modeling population to respondents aged 18–100 years to improve deployment realism and demographic consistency. Finally, cleaned datasets, feature metadata, leakage review artifacts, feature-type definitions, and reproducibility files were exported for downstream exploratory analysis and machine learning workflows.


