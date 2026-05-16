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
