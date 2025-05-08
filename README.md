# Predicting College Degree Completion by Age 22

## Project Overview
This project aims to predict whether children will complete a 4-year college degree by age 22 using data from the **Future of Families and Child Wellbeing Study (FFCWS)** Public Use Dataset (1998–2024). The target variable is **CK7EDU**, which represents the child's educational attainment by age 22.

## Key Features
- **Datasets**: Data files used for this analysis are too large to be uploaded, please retrive from https://www.childandfamilydataarchive.org/cfda/archives/cfda/studies/31622.
- **Data Cleaning & Preprocessing**: This includes handling missing values, encoding problematic data, and reducing dimensions.
- **Feature Selection**: Selected important features using Random Forest importance and XGboost. 
- **Modeling**: Random Forest was used as the primary model, with comparisons made to XGBoost.
- **Performance Metrics**: The model's performance was primarily evaluated using the F1 score, achieving a score of 0.91.

## Repository Structure
```plaintext
├── data/                # 14 datasets retrieved from https://www.childandfamilydataarchive.org/cfda/archives/cfda/studies/31622 
├── notebooks/           # Jupyter notebooks with analysis and model training steps
├── scripts/             # Python scripts of helper functions for data cleaning and feature selection
└── README.md            # This README file
