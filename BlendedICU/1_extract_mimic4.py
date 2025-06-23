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
from mimic4_preprocessing.mimic4preparator import mimic4Preparator

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent.absolute()

def parse_args():
    parser = argparse.ArgumentParser(description='Extract MIMIC-IV data')
    
    # Required paths
    parser.add_argument('--data-path', default=str(SCRIPT_DIR / 'data'),
                      help='Path to store processed data')
    
    # MIMIC-IV source paths with defaults
    parser.add_argument('--mimic4-source', default=str(SCRIPT_DIR / 'source' / 'mimic4'),
                      help='Path to MIMIC-IV source data')
    
    # Optional paths with defaults
    parser.add_argument('--auxillary-files', default=str(SCRIPT_DIR / 'auxillary_files'),
                      help='Path to auxillary files')
    parser.add_argument('--user-input', default=str(SCRIPT_DIR / 'auxillary_files/user_input'),
                      help='Path to user input files')
    parser.add_argument('--config', default=str(SCRIPT_DIR / 'config.json'),
                      help='Path to config file')
    
    return parser.parse_args()

def main():
    args = parse_args()
    
    # Create paths dictionary
    pth_dic = {
        "data_path": str(Path(args.data_path)),
        "mimic4_source_path": str(Path(args.mimic4_source)),
        "auxillary_files": str(Path(args.auxillary_files)),
        "user_input": str(Path(args.user_input)),
        "vocabulary": str(Path(args.auxillary_files) / 'OMOP_vocabulary'),
        "medication_mapping_files": str(Path(args.auxillary_files) / 'medication_mapping_files')
    }
    
    # Create MIMIC-IV preparator with relative paths from source directory
    mimic4_prep = mimic4Preparator(
        chartevents_pth=str(Path(args.mimic4_source) / 'icu/chartevents.csv.gz'),                         
        labevents_pth=str(Path(args.mimic4_source) / 'hosp/labevents.csv.gz'),
        d_labitems_pth=str(Path(args.mimic4_source) / 'hosp/d_labitems.csv.gz'),
        admissions_pth=str(Path(args.mimic4_source) / 'hosp/admissions.csv.gz'),
        diagnoses_pth=str(Path(args.mimic4_source) / 'hosp/diagnoses_icd.csv.gz'),
        d_diagnoses_pth=str(Path(args.mimic4_source) / 'hosp/d_icd_diagnoses.csv.gz'),
        d_items_pth=str(Path(args.mimic4_source) / 'icu/d_items.csv.gz'),
        inputevents_pth=str(Path(args.mimic4_source) / 'icu/inputevents.csv.gz'),
        outputevents_pth=str(Path(args.mimic4_source) / 'icu/outputevents.csv.gz'),
        icustays_pth=str(Path(args.mimic4_source) / 'icu/icustays.csv.gz'),
        patients_pth=str(Path(args.mimic4_source) / 'hosp/patients.csv.gz'),
        pth_dic=pth_dic,
        config_path=args.config)

    mimic4_prep.raw_tables_to_parquet()

    mimic4_prep.icustays = mimic4_prep.gen_icustays()
    mimic4_prep.gen_labels()
    mimic4_prep.gen_flat()
    mimic4_prep.gen_medication()
    mimic4_prep.gen_timeseriesoutputs()
    mimic4_prep.gen_timeserieslab()
    mimic4_prep.gen_timeseries()
    mimic4_prep.gen_diagnoses()

if __name__ == '__main__':
    main()
