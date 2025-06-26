"""
This code extracts the data from the MIMIC-IV dataset 
('mimic_source_path' in paths.json).

It creates a set of .parquet files at the specified path 
('mimic' in paths.json). 
Approximate running time: 20min.
"""
from mimic3_preprocessing.mimic3preparator import mimic3Preparator
from pathlib import Path
import yaml


mimic3_prep = mimic3Preparator(chartevents_pth='CHARTEVENTS.csv.gz',
                               d_labitems_pth='D_LABITEMS.csv.gz',
                               d_items_pth='D_ITEMS.csv.gz',
                               outputevents_pth='OUTPUTEVENTS.csv.gz',
                               icustays_pth='ICUSTAYS.csv.gz',
                               patients_pth='PATIENTS.csv.gz',
                               inputevents_mv_pth='INPUTEVENTS_MV.csv.gz',
                               inputevents_cv_pth='INPUTEVENTS_CV.csv.gz',
                               labevents_pth='LABEVENTS.csv.gz',
                               admissions_pth='ADMISSIONS.csv.gz')

mimic3_prep.raw_tables_to_parquet()

mimic3_prep.icustays = mimic3_prep.gen_icustays()
mimic3_prep.gen_labels()
mimic3_prep.gen_flat()
mimic3_prep.gen_medication()
mimic3_prep.gen_timeseriesoutputs()
mimic3_prep.gen_timeserieslab()
mimic3_prep.gen_timeseries()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Extract MIMIC-IV data")
    parser.add_argument("--pipe", action="store_true", help="Run in pipeline mode")
    parser.add_argument("--mimic3_source", help="Path to MIMIC-IV source data")
    parser.add_argument("--data_path", help="Path to store extracted data")
    parser.add_argument("--auxillary_files", help="Path to auxillary files")
    parser.add_argument("--user_input", help="Path to user input")
    parser.add_argument("--vocabulary", help="Path to OMOP vocabulary")
    parser.add_argument("--medication_mapping", help="Path to medication mapping files")
    args = parser.parse_args()

    if args.pipe:
        print("[INFO] Running in pipeline mode: loading all config from default paths.yaml in script directory")
        with open('paths.yaml', 'r') as f:
            paths = yaml.safe_load(f)
        mimic3_source = paths.get('mimic3_source')
        print(f"[INFO] mimic3_source: {mimic3_source}")
        data_path = paths.get('data_dir')
        auxillary_files = paths.get('auxillary_files')
        user_input = paths.get('user_input_dir')
        vocabulary = paths.get('omop_vocabulary_dir')
        medication_mapping = paths.get('medication_mapping_dir')
    else:
        print("[INFO] Running in standalone mode: using command-line arguments and defaults")
        mimic3_source = args.mimic3_source or str(Path('source') / 'mimic3')
        data_path = args.data_path or str(Path('data'))
        auxillary_files = args.auxillary_files or str(Path('auxillary_files'))
        user_input = args.user_input or str(Path('auxillary_files') / 'user_input')
        vocabulary = args.vocabulary or str(Path('auxillary_files') / 'OMOP_vocabulary')
        medication_mapping = args.medication_mapping or str(Path('auxillary_files') / 'medication_mapping_files')

    pth_dic = {
        "data_path": str(Path(data_path)),
        "mimic3_source_path": str(Path(mimic3_source)),
        "auxillary_files": str(Path(auxillary_files)),
        "user_input": str(Path(user_input)),
        "vocabulary": str(Path(vocabulary)),
        "medication_mapping_files": str(Path(medication_mapping))
    }
