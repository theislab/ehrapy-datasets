# Statlog (Heart) Data Set

## Description

This dataset contains the medical records of 270 patients, collected during their follow-up period, where each patient profile has 10 clinical features.\
Data Set Characteristics: Multivariate\
Number of Instances: 270\
Area: Life\
Attribute Characteristics: Real\
Number of Attributes: 13\
Date Donated: N/A\
Associated Tasks: Categorical/Classification\
Missing Values? No

## Columns
- age
- sex: one of (0, 1), 0 is female, 1 is male.
- chest: one of (1, 2, 3, 4), chest pain type.
- resting blood pressure
- serum_cholestoral: mg/dl
- fasting_blood_sugar: one of (0, 1), 0 is not > 120 mg/dl, 1 is > 120 mg/dl.
- resting_electrocardiographic_results: one of (0, 1, 2).
- maximum_heart_rate_achieved
- exercise_induced_angina: one of (0, 1), 0 is for "no", 1 is for "yes".
- oldpeak: ST depression induced by exercise relative to rest.
- slope: one of (1, 2, 3), the slope of the peak exercise ST segment.
- number of major vessels: one of (0, 1, 2, 3), colored by flourosopy.
- thal: one of (3, 6, 7), 3 is normal, 6 is fixed defect and 7 is reversable defect.
- [target] - Class: one of (0, 1), 0 is absence and 1 is presence.


## Source

http://archive.ics.uci.edu/ml/datasets/Statlog+%28Heart%29

## Modifications

1. Added a patient_id as the first column
2. Replaced the original encoding (1, 2) to (0, 1) in class attribute


