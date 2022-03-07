# Parkinson Dataset with replicated acoustic features Data Set

## Description

This dataset contains acoustic features extracted from 3 voice recording replications of the sustained a phonation for each one of the 80 subjects (40 of them with Parkinson's Disease).

Data Set Characteristics: Multivariate\
Number of Instances: 240\
Area: Life\
Attribute Characteristics: 	N/A\
Number of Attributes: 46\
Date Donated: 2019-04-10\
Associated Tasks: Classification\
Missing Values? N/A

## Columns
- ID: Subjects's identifier.
- Recording: Number of the recording.
- Status: 0=Healthy; 1=PD
- Gender: 0=Woman; 1=Man
- Pitch local perturbation measures: relative jitter (Jitter_rel), absolute jitter (Jitter_abs), relative average perturbation (Jitter_RAP), and pitch perturbation quotient (Jitter_PPQ).
- Amplitude perturbation measures: local shimmer (Shim_loc), shimmer in dB (Shim_dB), 3-point amplitude perturbation quotient (Shim_APQ3), 5-point amplitude perturbation quotient (Shim_APQ5), and 11-point amplitude perturbation quotient (Shim_APQ11).
- Harmonic-to-noise ratio measures: harmonic-to-noise ratio in the frequency band 0-500 Hz (HNR05), in 0-1500 Hz (HNR15), in 0-2500 Hz (HNR25), in 0-3500 Hz (HNR35), and in 0-3800 Hz (HNR38).
- Mel frequency cepstral coefficient-based spectral measures of order 0 to 12 (MFCC0, MFCC1,..., MFCC12) and their derivatives (Delta0, Delta1,..., Delta12).
- Recurrence period density entropy (RPDE).
- Detrended fluctuation analysis (DFA).
- Pitch period entropy (PPE).
- Glottal-to-noise excitation ratio (GNE).


## Source

http://archive.ics.uci.edu/ml/datasets/Parkinson+Dataset+with+replicated+acoustic+features+

## Modifications

1. Added a measurement_id as the first column
2. Changed Gender encoding to: 0=Woman; 1=Man