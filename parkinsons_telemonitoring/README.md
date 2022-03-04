# Parkinsons Telemonitoring Data Set

## Description

This dataset is composed of a range of biomedical voice measurements from 42 people with early-stage Parkinson's disease recruited to a six-month trial of a telemonitoring device for remote symptom progression monitoring. The recordings were automatically captured in the patient's homes. Columns in the table contain subject number, subject age, subject gender, time interval from baseline recruitment date, motor UPDRS, total UPDRS, and 16 biomedical voice measures. Each row corresponds to one of 5,875 voice recording from these individuals. The main aim of the data is to predict the motor and total UPDRS scores ('motor_UPDRS' and 'total_UPDRS') from the 16 voice measures.

Data Set Characteristics:  Multivariate\
Attribute Characteristics:  Integer, Real\
Associated Tasks:  Regression\
Number of Instances:  5875\
Number of Attributes:  26\
Area:  Life\
Date Donated:  2009-10-29\
Associated Tasks: Regression\
Missing Values? N/A

## Columns
- subject# - Integer that uniquely identifies each subject
- age - Subject age
- sex - Subject gender '0' - male, '1' - female
- test_time - Time since recruitment into the trial. The integer part is the number of days since recruitment.
- Jitter(%),Jitter(Abs),Jitter:RAP,Jitter:PPQ5,Jitter:DDP - Several measures of variation in fundamental frequency
- Shimmer,Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,Shimmer:APQ11,Shimmer:DDA - Several measures of variation in amplitude
- NHR,HNR - Two measures of ratio of noise to tonal components in the voice
- RPDE - A nonlinear dynamical complexity measure
- DFA - Signal fractal scaling exponent
- PPE - A nonlinear measure of fundamental frequency variation 
- [target] motor_UPDRS - Clinician's motor UPDRS score, linearly interpolated
- [target] total_UPDRS - Clinician's total UPDRS score, linearly interpolated


## Source

http://archive.ics.uci.edu/ml/datasets/Parkinsons+Telemonitoring

## Modifications

1. Added a measurement_id as the first column
