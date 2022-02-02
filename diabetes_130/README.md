# Diabetes 130-US hospitals for years 1999-2008 Data Set

## Description

This data has been prepared to analyze factors related to readmission as well as other outcomes pertaining to patients with diabetes.\
Data Set Characteristics: Multivariate\
Number of Instances: 100000\
Area: Life\
Attribute Characteristics: Integer\
Number of Attributes: 55\
Date Donated 2014-05-03\
Associated Tasks: Classification, Clustering\
Missing Values? Yes. ("?")\

## Columns

admission_type_id,description\
1,Emergency\
2,Urgent\
3,Elective\
4,Newborn\
5,Not Available\
6,NULL\
7,Trauma Center\
8,Not Mapped\
,

discharge_disposition_id,description\
1,Discharged to home\
2,Discharged/transferred to another short term hospital\
3,Discharged/transferred to SNF\
4,Discharged/transferred to ICF\
5,Discharged/transferred to another type of inpatient care institution\
6,Discharged/transferred to home with home health service\
7,Left AMA\
8,Discharged/transferred to home under care of Home IV provider\
9,Admitted as an inpatient to this hospital\
10,Neonate discharged to another hospital for neonatal aftercare\
11,Expired\
12,Still patient or expected to return for outpatient services\
13,Hospice / home\
14,Hospice / medical facility\
15,Discharged/transferred within this institution to Medicare approved swing bed\
16,Discharged/transferred/referred another institution for outpatient services\
17,Discharged/transferred/referred to this institution for outpatient services\
18,NULL\
19,"Expired at home. Medicaid only, hospice."\
20,"Expired in a medical facility. Medicaid only, hospice."\
21,"Expired, place unknown. Medicaid only, hospice."\
22,Discharged/transferred to another rehab fac including rehab units of a hospital .\
23,Discharged/transferred to a long term care hospital.\
24,Discharged/transferred to a nursing facility certified under Medicaid but not certified under Medicare.\
25,Not Mapped\
26,Unknown/Invalid\
30,Discharged/transferred to another Type of Health Care Institution not Defined Elsewhere\
27,Discharged/transferred to a federal health care facility.\
28,Discharged/transferred/referred to a psychiatric hospital of psychiatric distinct part unit of a hospital\
29,Discharged/transferred to a Critical Access Hospital (CAH).\
,

admission_source_id,description\
1, Physician Referral\
2,Clinic Referral\
3,HMO Referral\
4,Transfer from a hospital\
5, Transfer from a Skilled Nursing Facility (SNF)\
6, Transfer from another health care facility\
7, Emergency Room\
8, Court/Law Enforcement\
9, Not Available\
10, Transfer from critial access hospital\
11,Normal Delivery\
12, Premature Delivery\
13, Sick Baby\
14, Extramural Birth\
15,Not Available\
17,NULL\
18, Transfer From Another Home Health Agency\
19,Readmission to Same Home Health Agency\
20, Not Mapped\
21,Unknown/Invalid\
22, Transfer from hospital inpt/same fac result in a sep claim\
23, Born inside this hospital\
24, Born outside this hospital\
25, Transfer from Ambulatory Surgery Center\
26,Transfer from Hospice


## Source

http://archive.ics.uci.edu/ml/datasets/Diabetes+130-US+hospitals+for+years+1999-2008

## Modifications

1. Mapping gender to female -> 0, male -> 1, undefined -> NaN
2. Age and weight ranges were mapped to their means. e.g. [30-40] -> 35. All weights greater than 200 were mapped to the value 250.
3. Yes/No/Ch were mapped to boolean values
4. Map disease types to categories to have categorical and not numerical data in disease column map according to table 2 of paper https://downloads.hindawi.com/journals/bmri/2014/781670.pdf we'll do it for primary and secondary diagnosis separately.
5. Some columns are categorical but have multiple codes meaning "Unknown". Map them all to None, Data for that is taken from "IDs_mappings", Others map to their classes and store as categorical.
6. Rename columns time_in_hospital -> time_in_hospital_days, change -> change_of_meds, number_outpatient -> number_outpatient_visit, number_emergency -> number_emergency_visits, number_inpatient -> number_inpatient_visits
7. 