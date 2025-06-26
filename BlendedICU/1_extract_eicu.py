"""
This code extracts the data from the Amsterdam dataset 
('eicu_source_path' in paths.json).

It creates a set of .parquet files at the specified path 
('eicu' in paths.json). 
Approximate running time: 
    * raw_tables_to_parquet()  12min #only run once. csv.gz -> parquet with no data changes.
    * gen_* : 7min
"""
from eicu_preprocessing.eicupreparator import eicuPreparator
from pathlib import Path
import argparse
import yaml

def parse_args():
    parser = argparse.ArgumentParser(description="Extract data from the Amsterdam dataset")
    parser.add_argument("--pipe", action="store_true", help="Run in pipeline mode")
    parser.add_argument("--eicu_source", type=str, help="Path to the eicu source data")
    parser.add_argument("--data_path", type=str, help="Path to the data directory")
    parser.add_argument("--auxillary_files", type=str, help="Path to the auxillary files directory")
    parser.add_argument("--user_input", type=str, help="Path to the user input directory")
    parser.add_argument("--vocabulary", type=str, help="Path to the OMOP vocabulary directory")
    parser.add_argument("--medication_mapping", type=str, help="Path to the medication mapping files directory")
    return parser.parse_args()

args = parse_args()

if args.pipe:
    print("[INFO] Running in pipeline mode: loading all config from default paths.yaml in script directory")
    with open('paths.yaml', 'r') as f:
        paths = yaml.safe_load(f)
    eicu_source = paths.get('eicu_source')
    print(f"[INFO] eicu_source: {eicu_source}")
    data_path = paths.get('data_dir')
    auxillary_files = paths.get('auxillary_files')
    user_input = paths.get('user_input_dir')
    vocabulary = paths.get('omop_vocabulary_dir')
    medication_mapping = paths.get('medication_mapping_dir')
else:
    print("[INFO] Running in standalone mode: using command-line arguments and defaults")
    eicu_source = args.eicu_source or str(Path('source') / 'eicu')
    data_path = args.data_path or str(Path('data'))
    auxillary_files = args.auxillary_files or str(Path('auxillary_files'))
    user_input = args.user_input or str(Path('auxillary_files') / 'user_input')
    vocabulary = args.vocabulary or str(Path('auxillary_files') / 'OMOP_vocabulary')
    medication_mapping = args.medication_mapping or str(Path('auxillary_files') / 'medication_mapping_files')

pth_dic = {
    "data_path": str(Path(data_path)),
    "eicu_source_path": str(Path(eicu_source)),
    "auxillary_files": str(Path(auxillary_files)),
    "user_input": str(Path(user_input)),
    "vocabulary": str(Path(vocabulary)),
    "medication_mapping_files": str(Path(medication_mapping))
}

eicu_prep = eicuPreparator(
    physicalexam_pth='physicalExam.csv.gz',
    diag_pth='diagnosis.csv.gz',
    pasthistory_pth='pastHistory.csv.gz',
    admissiondx_pth='admissionDx.csv.gz',
    medication_pth='medication.csv.gz',
    infusiondrug_pth='infusionDrug.csv.gz',
    admissiondrug_pth='admissionDrug.csv.gz',
    patient_pth='patient.csv.gz',
    lab_pth='lab.csv.gz',
    respiratorycharting_pth='respiratoryCharting.csv.gz',
    nursecharting_pth='nurseCharting.csv.gz',
    periodic_pth='vitalPeriodic.csv.gz',
    aperiodic_pth='vitalAperiodic.csv.gz',
    intakeoutput_pth='intakeOutput.csv.gz')

eicu_prep.raw_tables_to_parquet()

eicu_prep.init_gen()
eicu_prep.gen_labels()
eicu_prep.gen_flat()
eicu_prep.gen_medication()
eicu_prep.gen_timeseriesintakeoutput()
eicu_prep.gen_timeseriesresp()
eicu_prep.gen_timeserieslab()
eicu_prep.gen_timeseriesnurse()
eicu_prep.gen_timeseriesaperiodic()
eicu_prep.gen_timeseriesperiodic()
