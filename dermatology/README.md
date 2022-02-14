# Dermatology Data Set

## Description

This dataset contains the medical records of 366 patients, collected during their follow-up period, where each patient profile has 33 clinical features.\
Data Set Characteristics: Multivariate\
Number of Instances: 366\
Area: Life\
Attribute Characteristics: Categorical/Integer\
Number of Attributes: 33\
Date Donated: 1998-01-01\
Associated Tasks: Classification\
Missing Values? Yes. 8 (in Age attribute). Distinguished with '?'.

## Data Set Information
The differential diagnosis of erythemato-squamous diseases is a real problem in dermatology. They all share the clinical features of erythema and scaling, with very little differences. The diseases in this group are psoriasis, seboreic dermatitis, lichen planus, pityriasis rosea, cronic dermatitis, and pityriasis rubra pilaris. Usually a biopsy is necessary for the diagnosis but unfortunately these diseases share many histopathological features as well. Another difficulty for the differential diagnosis is that a disease may show the features of another disease at the beginning stage and may have the characteristic features at the following stages. Patients were first evaluated clinically with 12 features. Afterwards, skin samples were taken for the evaluation of 22 histopathological features. The values of the histopathological features are determined by an analysis of the samples under a microscope.

In the dataset constructed for this domain, the family history feature has the value 1 if any of these diseases has been observed in the family, and 0 otherwise. The age feature simply represents the age of the patient. Every other feature (clinical and histopathological) was given a degree in the range of 0 to 3. Here, 0 indicates that the feature was not present, 3 indicates the largest amount possible, and 1, 2 indicate the relative intermediate values.

The names and id numbers of the patients were recently removed from the database.
## Columns

Clinical Attributes: (take values 0, 1, 2, 3, unless otherwise indicated)
- erythema
- scaling
- definite borders
- itching
- koebner phenomenon
- polygonal papules
- follicular papules
- oral mucosal involvement
- knee and elbow involvement
- scalp involvement
- family history, (0 or 1)
- Age (years)

Histopathological Attributes: (take values 0, 1, 2, 3)
- melanin incontinence
- eosinophils in the infiltrate
- PNL infiltrate
- fibrosis of the papillary dermis
- exocytosis
- acanthosis
- hyperkeratosis
- parakeratosis
- clubbing of the rete ridges
- elongation of the rete ridges
- thinning of the suprapapillary epidermis
- spongiform pustule
- munro microabcess
- focal hypergranulosis
- disappearance of the granular layer
- vacuolisation and damage of basal layer
- spongiosis
- saw-tooth appearance of retes
- follicular horn plug
- perifollicular parakeratosis
- inflammatory monoluclear inflitrate
- band-like infiltrate

[target] class: 
| class code | class                    | Number of instances |
|------------|--------------------------|---------------------|
| 1          | psoriasis                | 112                 |
| 2          | seboreic                 | 61                  |
| 3          | lichen planus            | 72                  |
| 4          | pityriasis rosea         | 49                  |
| 5          | cronic dermatitis        | 52                  |
| 6          | pityriasis rubra pilaris | 20                  |


## Source

http://archive.ics.uci.edu/ml/datasets/Dermatology

## Modifications

1. Added a patient_id as the first column
2. Converted age attribute to integer.
