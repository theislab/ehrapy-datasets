# Thyroid Data Set

## Description

This dataset contains the medical records of 7200 patients, collected during their follow-up period, where each patient profile has 21 clinical features.\
Data Set Characteristics: Multivariate, Domain-Theory\
Number of Instances: 7200\
Area: Life\
Attribute Characteristics: Categorical/Real\
Number of Attributes: 21\
Date Donated: 1987-01-01\
Associated Tasks: Classification\
Missing Values? Yes

## 
## Columns

- AGE: one of (10, 20, 30, 40, 50, 60, 70, 80)
- SEX: one of (0, 1). 0 is for "female", 1 is for "male".
- STEROID: one of (0, 1). 0 is for "no", 1 is for "yes".
- ANTIVIRALS: one of (0, 1). 0 is for "no", 1 is for "yes".
- FATIGUE: one of (0, 1). 0 is for "no", 1 is for "yes".
- MALAISE: one of (0, 1). 0 is for "no", 1 is for "yes".
- ANOREXIA: one of (0, 1). 0 is for "no", 1 is for "yes".
- LIVER BIG: one of (0, 1). 0 is for "no", 1 is for "yes".
- LIVER FIRM: one of (0, 1). 0 is for "no", 1 is for "yes".
- SPLEEN PALPABLE: one of (0, 1). 0 is for "no", 1 is for "yes".
- SPIDERS: one of (0, 1). 0 is for "no", 1 is for "yes".
- ASCITES: one of (0, 1). 0 is for "no", 1 is for "yes".
- VARICES: one of (0, 1). 0 is for "no", 1 is for "yes".
- BILIRUBIN: one of (0.39, 0.80, 1.20, 2.00, 3.00, 4.00)
- ALK PHOSPHATE: one of (33, 80, 120, 160, 200, 250)
- SGOT: one of (13, 100, 200, 300, 400, 500)
- ALBUMIN: one of (2.1, 3.0, 3.8, 4.5, 5.0, 6.0)
- PROTIME: one of (10, 20, 30, 40, 50, 60, 70, 80, 90)
- HISTOLOGY: one of (0, 1). 0 is for "no", 1 is for "yes".
- [target] - Class: one of (0, 1). 0 is for "LIVE", 1 is for "DIE". 


## Source

http://archive.ics.uci.edu/ml/datasets/Thyroid+Disease

## Modifications

1. Added a patient_id as the first column
2. Mapped female/male to 0 and 1 respectively.
3. Mapped no/yes to 0 and 1 respectively.
4. Mapped LIVE/DIE to 0 and 1 respectively.

