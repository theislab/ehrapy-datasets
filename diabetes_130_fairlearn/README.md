# Diabetes 130-US hospitals for years 1999-2008 Data Set Fairlearn

## Description

This data has been prepared to analyze factors related to readmission as well as other outcomes pertaining to patients with diabetes.\
Data Set Characteristics: Multivariate\
Number of Instances: 101766\
Area: Life\
Attribute Characteristics: Integer\
Number of Attributes: 24\
Date Donated (raw): 2014-05-03\
Associated Tasks: Classification, Clustering\
Missing Values? Yes.\

## Columns


- race: one of Caucasian, AfricanAmerican, Unknown, Hispanic, Other, Asian
- gender: one of Female, Male, Unknown/Invalid
- age: one of Over 60 years, 30-60 years, 30 years or younger
- discharge_disposition_id: one of Discharged to Home, Other
- admission_source_id: one of Emergency, Referral, Other,
- medical_specialty: one of Missing, Other, InternalMedicine, Emergency/Trauma, Family/GeneralPractice, Cardiology
- primary_diagnosis: one of Other, Respiratory, Issues, Diabetes, Genitourinary Issues, Musculoskeletal Issues
- max_glu_serum: one of Norm, >200, >300
- A1Cresult: one of >8, Norm, >7
- insulin: one of No, Steady, Down, Up
- change: one of No, Ch
- diabetesMed: one of Yes, No
- medicare: one of False, True
- medicaid: one of False, True		
- had_emergency: one of False, True	
- had_inpatient_days: one of False, True			
- had_outpatient_days: one of False, True		
- readmitted: one of NO, >30, <30
- readmit_binary: one of 0.000, 1.000
- readmit_30_days: one of 0.000, 1.000


## Source

Raw Data:
Clore,John, Cios,Krzysztof, DeShazo,Jon, and Strack,Beata. (2014). Diabetes 130-US Hospitals for Years 1999-2008. UCI Machine Learning Repository. https://doi.org/10.24432/C5230J.

http://archive.ics.uci.edu/ml/datasets/Diabetes+130-US+hospitals+for+years+1999-2008

Preprocessed Data:
Bird, S., Dudík, M., Edgar, R., Horn, B., Lutz, R., Milan, V., ... & Walker, K. (2020). Fairlearn: A toolkit for assessing and improving fairness in AI. Microsoft, Tech. Rep. MSR-TR-2020-32.
https://fairlearn.org/main/user_guide/datasets/diabetes_hospital_data.html


## Modifications
See link above.