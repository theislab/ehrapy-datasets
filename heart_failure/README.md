# Heart failure clinical records Data Set

## Description

This dataset contains the medical records of 299 patients who had heart failure, collected during their follow-up period, where each patient profile has 13 clinical features.\
Data Set Characteristics: Multivariate\
Number of Instances: 299\
Area: Life\
Attribute Characteristics: Integer/Real\
Number of Attributes: 13\
Date Donated 2020-02-05\
Associated Tasks: Classification, Clustering, Regression\
Missing Values? No. \

## Columns

- age: age of the patient (years)
- anaemia: decrease of red blood cells or hemoglobin (boolean)
- high blood pressure: if the patient has hypertension (boolean)
- creatinine phosphokinase (CPK): level of the CPK enzyme in the blood (mcg/L)
- diabetes: if the patient has diabetes (boolean)
- ejection fraction: percentage of blood leaving the heart at each contraction (percentage)
- platelets: platelets in the blood (kiloplatelets/mL)
- sex: woman or man (binary)
- serum creatinine: level of serum creatinine in the blood (mg/dL)
- serum sodium: level of serum sodium in the blood (mEq/L)
- smoking: if the patient smokes or not (boolean)
- time: follow-up period (days)
- [target] death event: if the patient deceased during the follow-up period (boolean) 

## Source

http://archive.ics.uci.edu/ml/datasets/Heart+failure+clinical+records#

## Modifications

1. Added a patient_id as the first column
