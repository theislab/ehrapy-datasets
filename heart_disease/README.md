# Heart Disease Data Set

## Description

This dataset contains the medical records of 303 patients, collected during their follow-up period, where each patient profile has 75 clinical features.\
Data Set Characteristics: Multivariate\
Number of Instances: 303\
Area: Life\
Attribute Characteristics: Categorical, Integer, Real\
Number of Attributes: 75\
Date Donated: 1988-07-01\
Associated Tasks: Classification\
Missing Values? Yes

## Columns
- age: age in years
- sex: one of (0, 1), 0 is female, 1 is male.
- cp: one of (1, 2, 3, 4), chest pain type. 1 is typical angina, 2 is atypical angina, 3 is non-anginal pain, and 4 is asymptomatic
- trestbps: resting blood pressure (in mm Hg on admission to the hospital)
- chol: serum cholestoral in mg/dl
- fbs: one of (0, 1), whether fasting blood sugar > 120 mg/dl or not. 1 is true, 0 is false
- restecg: one of (0, 1, 2), resting electrocardiographic results. 0 is normal, 1 is having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), and 2 is showing probable or definite left ventricular hypertrophy by Estes' criteria
- thalach: maximum heart rate achieved
- exang: one of (0, 1), exercise induced angina. 1 is yes and 0 is no
- oldpeak: ST depression induced by exercise relative to rest
- slope: one of (1, 2, 3), the slope of the peak exercise ST segment. 1 is upsloping, 2 is flat, 3 is downsloping
- ca: number of major vessels (0-3) colored by flourosopy
- thal: one of (3, 6, 7), 3 is normal, 6 is fixed defect, and 7 is reversable defect
- dataset_name - one of (cleveland, switzerland, hungarian, va), the origin database.  
- [target] - num: one of (0, 1), diagnosis of heart disease (angiographic disease status). 0: < 50% diameter narrowing, 1: > 50% diameter narrowing


## Source

http://archive.ics.uci.edu/ml/datasets/Heart+Disease

## Modifications

1. Added a patient_id as the first column
2. Replaced the original encoding (1, 2) to (0, 1) in class attribute
3. Added dataset_name to indicate the source of the dataset
