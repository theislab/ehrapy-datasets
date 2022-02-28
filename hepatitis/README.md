# Hepatitis Data Set

## Description

This dataset contains the medical records of 155 patients, collected during their follow-up period, where each patient profile has 19 clinical features.\
Data Set Characteristics: Multivariate\
Number of Instances: 155\
Area: Life\
Attribute Characteristics: Categorical/Integer/Real\
Number of Attributes: 19\
Date Donated: 1988-11-01\
Associated Tasks: Classification\
Missing Values? Yes

## Columns

- age: one of (10, 20, 30, 40, 50, 60, 70, 80)
- sex: one of (0, 1). 0 is for "female", 1 is for "male".
- steroid: one of (0, 1). 0 is for "no", 1 is for "yes".
- antivirals: one of (0, 1). 0 is for "no", 1 is for "yes".
- fatigue: one of (0, 1). 0 is for "no", 1 is for "yes".
- malaise: one of (0, 1). 0 is for "no", 1 is for "yes".
- anorexia: one of (0, 1). 0 is for "no", 1 is for "yes".
- liver big: one of (0, 1). 0 is for "no", 1 is for "yes".
- liver firm: one of (0, 1). 0 is for "no", 1 is for "yes".
- spleen palpable: one of (0, 1). 0 is for "no", 1 is for "yes".
- spiders: one of (0, 1). 0 is for "no", 1 is for "yes".
- ascites: one of (0, 1). 0 is for "no", 1 is for "yes".
- varices: one of (0, 1). 0 is for "no", 1 is for "yes".
- bilirubin: one of (0.39, 0.80, 1.20, 2.00, 3.00, 4.00)
- alk phosphate: one of (33, 80, 120, 160, 200, 250)
- sgot: one of (13, 100, 200, 300, 400, 500)
- albumin: one of (2.1, 3.0, 3.8, 4.5, 5.0, 6.0)
- protime: one of (10, 20, 30, 40, 50, 60, 70, 80, 90)
- histology: one of (0, 1). 0 is for "no", 1 is for "yes".
- [target] - class: one of (0, 1). 0 is for "live", 1 is for "die". 


## Source

http://archive.ics.uci.edu/ml/datasets/Hepatitis

## Modifications

1. Added a patient_id as the first column
2. Mapped female/male to 0 and 1 respectively.
3. Mapped no/yes to 0 and 1 respectively.
4. Mapped live/die to 0 and 1 respectively.

