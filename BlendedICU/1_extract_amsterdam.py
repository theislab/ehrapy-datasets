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
from pathlib import Path
import argparse
import yaml

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Extract Amsterdam dataset")
parser.add_argument("--pipe", action="store_true", help="Run in pipeline mode")
parser.add_argument("--amsterdam_source", type=str, help="Path to Amsterdam source data")
parser.add_argument("--data_path", type=str, help="Path to data directory")
parser.add_argument("--auxillary_files", type=str, help="Path to auxillary files")
parser.add_argument("--user_input", type=str, help="Path to user input directory")
parser.add_argument("--vocabulary", type=str, help="Path to OMOP vocabulary directory")
parser.add_argument("--medication_mapping", type=str, help="Path to medication mapping files")
args = parser.parse_args()

if args.pipe:
    print("[INFO] Running in pipeline mode: loading all config from default paths.yaml in script directory")
    with open('paths.yaml', 'r') as f:
        paths = yaml.safe_load(f)
    amsterdam_source = paths.get('amsterdam_source')
    print(f"[INFO] amsterdam_source: {amsterdam_source}")
    data_path = paths.get('data_dir')
    auxillary_files = paths.get('auxillary_files')
    user_input = paths.get('user_input_dir')
    vocabulary = paths.get('omop_vocabulary_dir')
    medication_mapping = paths.get('medication_mapping_dir')
else:
    print("[INFO] Running in standalone mode: using command-line arguments and defaults")
    amsterdam_source = args.amsterdam_source or str(Path('source') / 'amsterdam')
    data_path = args.data_path or str(Path('data'))
    auxillary_files = args.auxillary_files or str(Path('auxillary_files'))
    user_input = args.user_input or str(Path('auxillary_files') / 'user_input')
    vocabulary = args.vocabulary or str(Path('auxillary_files') / 'OMOP_vocabulary')
    medication_mapping = args.medication_mapping or str(Path('auxillary_files') / 'medication_mapping_files')

pth_dic = {
    "data_path": str(Path(data_path)),
    "amsterdam_source_path": str(Path(amsterdam_source)),
    "auxillary_files": str(Path(auxillary_files)),
    "user_input": str(Path(user_input)),
    "vocabulary": str(Path(vocabulary)),
    "medication_mapping_files": str(Path(medication_mapping))
}

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
