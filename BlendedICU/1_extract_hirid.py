"""
This code extracts the data from the Amsterdam dataset 
('hirid_source_path' in paths.json).

It creates a set of .parquet files at the specified path 
('hirid' in paths.json). 

"""
from hirid_preprocessing.HiridPreparator import hiridPreparator
from pathlib import Path
import argparse
import yaml

def parse_args():
    parser = argparse.ArgumentParser(description="Extract data from the Amsterdam dataset")
    parser.add_argument("--pipe", action="store_true", help="Run in pipeline mode")
    parser.add_argument("--hirid_source", help="Path to the hirid source")
    parser.add_argument("--data_path", help="Path to the data directory")
    parser.add_argument("--auxillary_files", help="Path to the auxillary files directory")
    parser.add_argument("--user_input", help="Path to the user input directory")
    parser.add_argument("--vocabulary", help="Path to the vocabulary directory")
    parser.add_argument("--medication_mapping", help="Path to the medication mapping directory")
    return parser.parse_args()

args = parse_args()

if args.pipe:
    print("[INFO] Running in pipeline mode: loading all config from default paths.yaml in script directory")
    with open('paths.yaml', 'r') as f:
        paths = yaml.safe_load(f)
    hirid_source = paths.get('hirid_source')
    print(f"[INFO] hirid_source: {hirid_source}")
    data_path = paths.get('data_dir')
    auxillary_files = paths.get('auxillary_files')
    user_input = paths.get('user_input_dir')
    vocabulary = paths.get('omop_vocabulary_dir')
    medication_mapping = paths.get('medication_mapping_dir')
else:
    print("[INFO] Running in standalone mode: using command-line arguments and defaults")
    hirid_source = args.hirid_source or str(Path('source') / 'hirid')
    data_path = args.data_path or str(Path('data'))
    auxillary_files = args.auxillary_files or str(Path('auxillary_files'))
    user_input = args.user_input or str(Path('auxillary_files') / 'user_input')
    vocabulary = args.vocabulary or str(Path('auxillary_files') / 'OMOP_vocabulary')
    medication_mapping = args.medication_mapping or str(Path('auxillary_files') / 'medication_mapping_files')

pth_dic = {
    "data_path": str(Path(data_path)),
    "hirid_source_path": str(Path(hirid_source)),
    "auxillary_files": str(Path(auxillary_files)),
    "user_input": str(Path(user_input)),
    "vocabulary": str(Path(vocabulary)),
    "medication_mapping_files": str(Path(medication_mapping))
}

hirid_prep = hiridPreparator(
    variable_ref_path='hirid_variable_reference_v1.csv',
    ts_path='observation_tables/parquet/',
    pharma_path='pharma_records/parquet/',
    admissions_path='reference_data/general_table.csv',
    imputedstage_path='imputed_stage/parquet/')

hirid_prep.raw_tables_to_parquet()

hirid_prep.init_gen()
hirid_prep.gen_labels()
hirid_prep.gen_medication()
hirid_prep.gen_timeseries()
