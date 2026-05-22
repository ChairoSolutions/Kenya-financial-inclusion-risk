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
