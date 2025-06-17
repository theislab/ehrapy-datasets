"""
This code extracts the data from the Amsterdam dataset 
('amsterdam_source_path' in paths.json).

It creates a set of .parquet files at the specified path 
('amsterdam' in paths.json). 
Approximate running time: 
    * raw_tables_to_parquet()  30min #only run once. csv.gz -> parquet with no data changes.
    * gen_* : 11min
"""
from amsterdam_preprocessing.AmsterdamPreparator import AmsterdamPreparator

ams_prep = AmsterdamPreparator(
    admission_pth='admissions.csv.gz',
    drugitems_pth='drugitems.csv.gz',
    numericitems_pth='numericitems.csv.gz',
    listitems_pth='listitems.csv.gz')

ams_prep.raw_tables_to_parquet()

ams_prep.gen_labels()
ams_prep.gen_medication()
ams_prep.gen_listitems_timeseries()
ams_prep.gen_num_timeseries()
