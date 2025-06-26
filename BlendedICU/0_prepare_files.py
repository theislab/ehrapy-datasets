'''
This code generates the mapping between ingredients from the OMOP standard
vocabulary and the drugnames in the source databases.

The omop_medication module creates a ohdsi_icu_medications.csv table
which contains brand names for a number of ingredients.
This file can be completed by a manual_icu_meds.csv file that lists additional
ingredients or additional synonyms or brand names for an ingredient in the
ohdsi vocabulary.

The medication_mapping module searches the labels in the source databases
and creates a json file listing all labels associated to an ingredient for each
source database.
'''
import json
import argparse
from pathlib import Path
import yaml  # For YAML path config support

from omopize.omop_medications import OMOP_Medications
from omopize.medication_mapping import MedicationMapping
from omopize.omop_diagnoses import DiagnosesMapping
from omop_cdm import omop_parquet 

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent.absolute()

def load_paths(paths_path):
    if paths_path and Path(paths_path).is_file():
        with open(paths_path, 'r') as f:
            return yaml.safe_load(f)
    return {}

def parse_args():
    parser = argparse.ArgumentParser(description='Prepare files for BlendedICU dataset processing')
    parser.add_argument('--pipe', action='store_true', help='If set, load all config from paths.yaml and ignore other args')
    parser.add_argument('--paths', default='paths.yaml', help='Path to paths.yaml (for path config)')
    parser.add_argument('--data-path', help='Path to store processed data')
    parser.add_argument('--source-dir', help='Base directory containing all source data in standardized subdirectories (mimic4, mimic3, eicu, amsterdam, hirid)')
    parser.add_argument('--mimic4-source', help='Path to MIMIC-IV source data (overrides source-dir/mimic4)')
    parser.add_argument('--mimic3-source', help='Path to MIMIC-III source data (overrides source-dir/mimic3)')
    parser.add_argument('--eicu-source', help='Path to eICU source data (overrides source-dir/eicu)')
    parser.add_argument('--amsterdam-source', help='Path to Amsterdam source data (overrides source-dir/amsterdam)')
    parser.add_argument('--hirid-source', help='Path to HiRID source data (overrides source-dir/hirid)')
    parser.add_argument('--auxillary-files', help='Path to auxillary files')
    parser.add_argument('--vocabulary', help='Path to OMOP vocabulary')
    parser.add_argument('--user-input', help='Path to user input files')
    parser.add_argument('--medication-mapping', help='Path to medication mapping files')
    return parser.parse_args()

def get_source_path(args, source_name):
    """Get the source path, using individual override if specified, otherwise using source-dir."""
    individual_path = getattr(args, f'{source_name}_source', None)
    if individual_path:
        return str(Path(individual_path))
    return str(Path(args.source_dir) / source_name)

def main():
    args = parse_args()
    if args.pipe:
        print("[INFO] Running in pipeline mode: loading all config from paths.yaml in script directory")
        import yaml
        with open('paths.yaml', 'r') as f:
            paths = yaml.safe_load(f)
        data_path = paths.get('data_dir')
        mimic4_source = paths.get('mimic4_source')
        mimic3_source = paths.get('mimic3_source')
        eicu_source = paths.get('eicu_source')
        amsterdam_source = paths.get('amsterdam_source')
        hirid_source = paths.get('hirid_source')
        auxillary_files = paths.get('auxillary_files')
        vocabulary = paths.get('omop_vocabulary_dir')
        user_input = paths.get('user_input_dir')
        medication_mapping = paths.get('medication_mapping_dir')
        selected_datasets = paths.get('selected_datasets', ['hirid', 'amsterdam', 'mimic4', 'mimic3', 'eicu'])
    else:
        print("[INFO] Running in standalone mode: using command-line arguments and defaults")
        data_path = args.data_path or str(SCRIPT_DIR / 'data')
        mimic4_source = args.mimic4_source or str(SCRIPT_DIR / 'source' / 'mimic4')
        mimic3_source = args.mimic3_source or str(SCRIPT_DIR / 'source' / 'mimic3')
        eicu_source = args.eicu_source or str(SCRIPT_DIR / 'source' / 'eicu')
        amsterdam_source = args.amsterdam_source or str(SCRIPT_DIR / 'source' / 'amsterdam')
        hirid_source = args.hirid_source or str(SCRIPT_DIR / 'source' / 'hirid')
        auxillary_files = args.auxillary_files or str(SCRIPT_DIR / 'auxillary_files')
        vocabulary = args.vocabulary or str(SCRIPT_DIR / 'auxillary_files/OMOP_vocabulary')
        user_input = args.user_input or str(SCRIPT_DIR / 'auxillary_files/user_input')
        medication_mapping = args.medication_mapping or str(SCRIPT_DIR / 'auxillary_files/medication_mapping_files')
        selected_datasets = ['hirid', 'amsterdam', 'mimic4', 'mimic3', 'eicu']

    pth_dic = {
        "data_path": str(Path(data_path)),
        "mimic4_source_path": str(Path(mimic4_source)),
        "mimic3_source_path": str(Path(mimic3_source)),
        "eicu_source_path": str(Path(eicu_source)),
        "amsterdam_source_path": str(Path(amsterdam_source)),
        "hirid_source_path": str(Path(hirid_source)),
        "auxillary_files": str(Path(auxillary_files)),
        "vocabulary": str(Path(vocabulary)),
        "user_input": str(Path(user_input)),
        "medication_mapping_files": str(Path(medication_mapping))
    }

    # Convert paths to parquet
    omop_parquet.convert_to_parquet(pth_dic)

    # Generate medication mappings for selected datasets
    om = OMOP_Medications(pth_dic)
    ingredient_to_drug = om.run()

    mm = MedicationMapping(pth_dic, datasets=selected_datasets)
    medication_json = mm.run(load_drugnames=False, fname='medications.json')

    # Generate diagnoses mappings for selected datasets (if needed)
    dm = DiagnosesMapping(pth_dic, datasets=selected_datasets)

if __name__ == '__main__':
    main()
