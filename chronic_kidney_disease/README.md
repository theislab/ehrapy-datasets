# Chronic Kidney Disease Data Set

## Description

This dataset contains the medical records of 400 patients, in which 250 patients are with Chronic Kidney Disease and the other 150 are without Chronic Kidney Disease. Each patient profile has 25 clinical features, including one target (Class).\
Data Set Characteristics: Multivariate\
Number of Instances: 400\
Area: Life\
Attribute Characteristics: Integer/Float/Real\
Number of Attributes: 25\
Date Donated July 2015\
Associated Tasks: Classification, Clustering\
Missing Values? Yes.

## Columns

- Age: age in years
- Blood Pressure: BP in mm/Hg (MB: presumably diastolic blood pressure)
- Specific Gravity: one of (1.005, 1.010, 1.015, 1.020, 1.025)
- Albumin: one of (0, 1, 2, 3, 4, 5)
- Sugar: one of (0, 1, 2, 3, 4, 5)
- Red Blood Cells: one of (0, 1). 0 is for "normal", 1 is for "abnormal".
- Pus Cell: one of (0, 1). 0 is for "normal", 1 is for "abnormal".
- Pus Cell clumps: one of (0, 1). 0 is for "notpresent", 1 is for "present".
- Bacteria: one of (0, 1). 0 is for "notpresent", 1 is for "present".
- Blood Glucose Random: in mgs/dl
- Blood Urea: in mgs/dl
- Serum Creatinine: in mgs/dl
- Sodium: in mEq/L
- Potassium: in mEq/L
- Hemoglobin: in gms
- Packed Cell Volume
- White Blood Cell Count: in cells/cumm
- Red Blood Cell Count: in millions/cmm
- Hypertension: one of (0, 1). 0 is for "no", 1 is for "yes".
- Diabetes Mellitus: one of (0, 1). 0 is for "no", 1 is for "yes". 
- Coronary Artery Disease: one of (0, 1). 0 is for "no", 1 is for "yes". 
- Appetite: one of (0, 1). 0 is for "good", 1 is for "poor".
- Pedal Edema: one of (0, 1). 0 is for "no", 1 is for "yes". 
- Anemia: one of (0, 1). 0 is for "no", 1 is for "yes". 
- [target] Class : one of (0, 1). 0 is for "Not Chronic Kidney Disease", 1 is for "Chronic Kidney Disease". 

## Source

https://archive.ics.uci.edu/ml/datasets/Chronic_Kidney_Disease#    
https://github.com/odsti/datasets/tree/master/ckd

## Modifications

1. Added a patient_id as the first column
2. Mapped normal/abnormal to 0 and 1 respectively.
3. Mapped notpresent and present to 0 and 1 respectively.
4. Mapped no/yes to 0 and 1 respectively.
5. Mapped good/poor to 0 and 1 respectively.
6. Mapped notckd and ckd to 0 and 1 respectively.
