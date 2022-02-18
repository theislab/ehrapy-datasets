# Breast Tissue Data Set

## Description

This dataset contains the medical records of 106 patients, collected during their follow-up period, where each patient profile has 10 clinical features.\
Data Set Characteristics: Multivariate\
Number of Instances: 106\
Area: Life\
Attribute Characteristics: Real\
Number of Attributes: 10\
Date Donated: 2010-05-10\
Associated Tasks: Classification\
Missing Values? No

## Columns
- I0: I0 Impedivity (ohm) at zero frequency
- PA500: PA500 phase angle at 500 KHz
- HFS: HFS high-frequency slope of phase angle
- DA: DA impedance distance between spectral ends
- Area: AREA area under spectrum
- A/DA: A/DA area normalized by DA
- Max IP: MAX IP maximum of the spectrum
- DR: DR distance between I0 and real part of the maximum frequency point
- P: P length of the spectral curve
- [target] - Class: one of ('car', 'fad', 'mas', 'gla', 'con', 'adi'), car (carcinoma), fad (fibro-adenoma), mas (mastopathy), gla (glandular), con (connective), adi (adipose).


## Source

http://archive.ics.uci.edu/ml/datasets/Breast+Tissue

## Modifications

1. Added a patient_id as the first column


