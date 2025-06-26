"""
This code extracts the data from the MIMIC-IV dataset 
('mimic_source_path' in paths.json).

It creates a set of .parquet files at the specified path 
('mimic' in paths.json). 
Approximate running time: 
    * raw_tables_to_parquet()  19min #only run once. csv.gz -> parquet with no data changes.
    * gen_* : 1min
"""
import argparse
from pathlib import Path
import yaml
import sys
#from mimic4_preprocessing.mimic4preparator import mimic4Preparator

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent.absolute()

def load_paths(paths_path):
    if paths_path and Path(paths_path).is_file():
        with open(paths_path, 'r') as f:
            return yaml.safe_load(f)
    return {}

def parse_args():
    parser = argparse.ArgumentParser(description='Extract MIMIC-IV data')
    parser.add_argument('--pipe', action='store_true', help='If set, load all config from paths.yaml and ignore other args')
    parser.add_argument('--config', default='config.json', help='Path to config.json (optional, for future use)')
    parser.add_argument('--paths', default='paths.yaml', help='Path to paths.yaml (for path config)')
    parser.add_argument('--data-path', help='Path to store processed data')
    parser.add_argument('--mimic4-source', help='Path to MIMIC-IV source data')
    parser.add_argument('--auxillary-files', help='Path to auxillary files')
    parser.add_argument('--user-input', help='Path to user input files')
    parser.add_argument('--vocabulary', help='Path to OMOP vocabulary')
    parser.add_argument('--medication-mapping', help='Path to medication mapping files')
    return parser.parse_args()

def main():
    args = parse_args()
    if args.pipe:
        print("[INFO] Running in pipeline mode: loading all config from default paths.yaml in script directory")
        import yaml
        with open('paths.yaml', 'r') as f:
            paths = yaml.safe_load(f)
        mimic4_source = paths.get('mimic4_source')
        print(f"[INFO] mimic4_source: {mimic4_source}")
        data_path = paths.get('data_dir')
        auxillary_files = paths.get('auxillary_files')
        user_input = paths.get('user_input_dir')
        vocabulary = paths.get('omop_vocabulary_dir')
        medication_mapping = paths.get('medication_mapping_dir')
    else:
        print("[INFO] Running in standalone mode: using command-line arguments and defaults")
        mimic4_source = args.mimic4_source or str(SCRIPT_DIR / 'source' / 'mimic4')
        data_path = args.data_path or str(SCRIPT_DIR / 'data')
        auxillary_files = args.auxillary_files or str(SCRIPT_DIR / 'auxillary_files')
        user_input = args.user_input or str(SCRIPT_DIR / 'auxillary_files' / 'user_input')
        vocabulary = args.vocabulary or str(SCRIPT_DIR / 'auxillary_files' / 'OMOP_vocabulary')
        medication_mapping = args.medication_mapping or str(SCRIPT_DIR / 'auxillary_files' / 'medication_mapping_files')

    pth_dic = {
        "data_path": str(Path(data_path)),
        "mimic4_source_path": str(Path(mimic4_source)),
        "auxillary_files": str(Path(auxillary_files)),
        "user_input": str(Path(user_input)),
        "vocabulary": str(Path(vocabulary)),
        "medication_mapping_files": str(Path(medication_mapping))
    }

    print("[INFO] Initializing mimic4Preparator...")
    from mimic4_preprocessing.mimic4preparator import mimic4Preparator
    mimic4_prep = mimic4Preparator(
        chartevents_pth='icu/chartevents.csv.gz',
        labevents_pth='hosp/labevents.csv.gz',
        d_labitems_pth='hosp/d_labitems.csv.gz',
        admissions_pth='hosp/admissions.csv.gz',
        diagnoses_pth='hosp/diagnoses_icd.csv.gz',
        d_diagnoses_pth='hosp/d_icd_diagnoses.csv.gz',
        d_items_pth='icu/d_items.csv.gz',
        inputevents_pth='icu/inputevents.csv.gz',
        outputevents_pth='icu/outputevents.csv.gz',
        icustays_pth='icu/icustays.csv.gz',
        patients_pth='hosp/patients.csv.gz',
        pth_dic=pth_dic,
        config_path=args.config)
    print("[INFO] mimic4Preparator initialized.")

    print("[INFO] Running raw_tables_to_parquet()...")
    mimic4_prep.raw_tables_to_parquet()
    print("[INFO] Finished raw_tables_to_parquet().")

    print("[INFO] Running gen_icustays()...")
    mimic4_prep.icustays = mimic4_prep.gen_icustays()
    print("[INFO] Finished gen_icustays().")

    print("[INFO] Running gen_labels()...")
    mimic4_prep.gen_labels()
    print("[INFO] Finished gen_labels().")

    print("[INFO] Running gen_flat()...")
    mimic4_prep.gen_flat()
    print("[INFO] Finished gen_flat().")

    print("[INFO] Running gen_medication()...")
    mimic4_prep.gen_medication()
    print("[INFO] Finished gen_medication().")

    print("[INFO] Running gen_timeseriesoutputs()...")
    mimic4_prep.gen_timeseriesoutputs()
    print("[INFO] Finished gen_timeseriesoutputs().")

    print("[INFO] Running gen_timeserieslab()...")
    mimic4_prep.gen_timeserieslab()
    print("[INFO] Finished gen_timeserieslab().")

    print("[INFO] Running gen_timeseries()...")
    mimic4_prep.gen_timeseries()
    print("[INFO] Finished gen_timeseries().")

    print("[INFO] Running gen_diagnoses()...")
    mimic4_prep.gen_diagnoses()
    print("[INFO] Finished gen_diagnoses().")

if __name__ == '__main__':
    main()
