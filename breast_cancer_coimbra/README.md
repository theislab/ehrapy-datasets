# Breast Cancer Coimbra Data Set

## Description

This dataset contains the clinical features were observed or measured for 64 patients with breast cancer and 52 healthy controls. There are 10 predictors, all quantitative, and a binary dependent variable, indicating the presence or absence of breast cancer. The predictors are anthropometric data and parameters which can be gathered in routine blood analysis.
Prediction models based on these predictors, if accurate, can potentially be used as a biomarker of breast cancer.\
Data Set Characteristics: Multivariate\
Number of Instances: 116\
Area: Life\
Attribute Characteristics: Integer\
Number of Attributes: 10\
Date Donated: 2018-03-06\
Associated Tasks: Classification\
Missing Values? No

## Columns
- Age: years
- BMI: $kg/m^2$
- Glucose: mg/dL
- Insulin: µU/mL
- HOMA
- Leptin: ng/mL
- Adiponectin: µg/mL
- Resistin: ng/mL
- MCP-1: pg/dL
- [target] - Class: one of (1, 2). 1=Healthy controls
2=Patients.


## Source

http://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Coimbra

## Modifications

1. Added a patient_id as the first column.
2. Changed column name of "Classification" to "Class".