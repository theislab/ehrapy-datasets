# Echocardiogram Data Set

## Description

This dataset contains the medical records of 132 patients who suffered heart attacks at some point in the past, collected during their follow-up period, where each patient profile has 12 clinical features.\
Data Set Characteristics: Multivariate\
Number of Instances: 132\
Area: Life\
Attribute Characteristics: Categorical/Integer/Real\
Number of Attributes: 12\
Date Donated: 1989-02-28\
Associated Tasks: Classification\
Missing Values? Yes

## Columns

- survival -- the number of months patient survived (has survived, if patient is still alive). Because all the patients had their heart attacks at different times, it is possible that some patients have survived less than one year but they are still alive. Check the second variable to confirm this. Such patients cannot be used for the prediction task mentioned above.
- still-alive -- a binary variable. 0=dead at end of survival period, 1 means still alive
- age-at-heart-attack -- age in years when heart attack occurred
- pericardial-effusion -- binary. Pericardial effusion is fluid around the heart. 0=no fluid, 1=fluid
- fractional-shortening -- a measure of contracility around the heart lower numbers are increasingly abnormal
- epss -- E-point septal separation, another measure of contractility. Larger numbers are increasingly abnormal.
- lvdd -- left ventricular end-diastolic dimension. This is a measure of the size of the heart at end-diastole. Large hearts tend to be sick hearts.
- wall-motion-score -- a measure of how the segments of the left ventricle are moving
- wall-motion-index -- equals wall-motion-score divided by number of segments seen. Usually 12-13 segments are seen in an echocardiogram. Use this variable INSTEAD of the wall motion score.
- mult -- a derivate var which can be ignored
- name -- the name of the patient which can be ignored
- group -- meaningless which can be ignored
- [target] alive-at-1 -- Derived from attribute survival and still-alive. 0 means patient was either dead after 1 year or had been followed for less than 1 year. 1 means patient was alive at 1 year. (boolean)


## Source

http://archive.ics.uci.edu/ml/datasets/Echocardiogram

## Modifications

1. Added a patient_id as the first column
2. Ignored meaningless columns, include "mult", "name", "group"
