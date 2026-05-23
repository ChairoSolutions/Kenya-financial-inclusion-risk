# Explainability & Interpretability Analysis

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
