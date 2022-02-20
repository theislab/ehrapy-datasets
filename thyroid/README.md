# Thyroid Data Set

## Description

This dataset contains the medical records related to thyroid diease, collected during their follow-up period.\
Data Set Characteristics: Multivariate, Domain-Theory\
Number of Instances: 7200\
Area: Life\
Attribute Characteristics: Categorical/Real\
Number of Attributes: 21\
Date Donated: 1987-01-01\
Associated Tasks: Classification\
Missing Values? Yes

## Columns
- age
- sex: one of (0, 1), 0 is female, 1 is male.
- on thyroxine: one of (0, 1), 0 is false, 1 is true.
- query on thyroxine: one of (0, 1), 0 is false, 1 is true.
- on antithyroid medication: one of (0, 1), 0 is false, 1 is true.
- sick: one of (0, 1), 0 is false, 1 is true.
- pregnant: one of (0, 1), 0 is false, 1 is true.
- thyroid surgery: one of (0, 1), 0 is false, 1 is true.
- I131 treatment: one of (0, 1), 0 is false, 1 is true.
- query hypothyroid: one of (0, 1), 0 is false, 1 is true.
- query hyperthyroid: one of (0, 1), 0 is false, 1 is true.
- lithium: one of (0, 1), 0 is false, 1 is true.
- goitre: one of (0, 1), 0 is false, 1 is true.
- tumor: one of (0, 1), 0 is false, 1 is true.
- hypopituitary: one of (0, 1), 0 is false, 1 is true.
- psych: one of (0, 1), 0 is false, 1 is true.
- TSH measured: one of (0, 1), 0 is false, 1 is true.
- TSH: continuous.
- T3 measured: one of (0, 1), 0 is false, 1 is true.
- T3: continuous.
- TT4 measured: one of (0, 1), 0 is false, 1 is true.
- TT4: continuous.
- T4U measured: one of (0, 1), 0 is false, 1 is true.
- T4U: continuous.
- FTI measured: one of (0, 1), 0 is false, 1 is true.
- FTI: continuous.
- TBG measured: one of (0, 1), 0 is false, 1 is true.
- TBG: continuous.
- referral source: WEST, STMW, SVHC, SVI, SVHD, other.

## Classes/Target
### Thyroid-allbp dataset
- increased binding protein, 
- decreased binding protein, 
- negative
### Thyroid-allhyper dataset
- hyperthyroid, 
- T3 toxic, 
- goitre, 
- secondary toxic, 
- negative
### Thyroid-allhypo dataset
- hypothyroid, 
- primary hypothyroid, 
- compensated hypothyroid, 
- secondary hypothyroid, 
- negative
### Thyroid-allrep dataset
- replacement therapy, 
- underreplacement, 
- overreplacement,
- negative
### Thyroid-dis dataset
- discordant, 
- negative
### Thyroid-sick dataset
- sick, 
- negative

## Source

http://archive.ics.uci.edu/ml/datasets/Thyroid+Disease

## Modifications

1. Added a patient_id as the first column
2. Mapped 'f'/'t' to 0 and 1 respectively.
3. Mapped 'F'/'M' to 0 and 1 respectively.
4. Replace "?"(missing value) with NaN and convert from object type to numeric type.
5. Deleted "TBG" attribute from original dataset, because all the data are missing.
6. Deleted "id" (patient id number) from the original dataset.