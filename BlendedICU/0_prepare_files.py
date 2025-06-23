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

from omopize.omop_medications import OMOP_Medications
from omopize.medication_mapping import MedicationMapping
from omopize.omop_diagnoses import DiagnosesMapping
from omop_cdm import omop_parquet 

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent.absolute()

def parse_args():
    parser = argparse.ArgumentParser(description='Prepare files for BlendedICU dataset processing')
    
    # Required base paths
    parser.add_argument('--data-path', default=str(SCRIPT_DIR / 'data'),
                      help='Path to store processed data')
    parser.add_argument('--source-dir', default=str(SCRIPT_DIR / 'source'),
                      help='Base directory containing all source data in standardized subdirectories (mimic4, mimic3, eicu, amsterdam, hirid)')
    
    # Optional individual source paths (will override source-dir if specified)
    parser.add_argument('--mimic4-source', help='Path to MIMIC-IV source data (overrides source-dir/mimic4)')
    parser.add_argument('--mimic3-source', help='Path to MIMIC-III source data (overrides source-dir/mimic3)')
    parser.add_argument('--eicu-source', help='Path to eICU source data (overrides source-dir/eicu)')
    parser.add_argument('--amsterdam-source', help='Path to Amsterdam source data (overrides source-dir/amsterdam)')
    parser.add_argument('--hirid-source', help='Path to HiRID source data (overrides source-dir/hirid)')
    
    # Optional paths with defaults
    parser.add_argument('--auxillary-files', default=str(SCRIPT_DIR / 'auxillary_files'),
                      help='Path to auxillary files')
    parser.add_argument('--vocabulary', default=str(SCRIPT_DIR / 'auxillary_files/OMOP_vocabulary'),
                      help='Path to OMOP vocabulary')
    parser.add_argument('--user-input', default=str(SCRIPT_DIR / 'auxillary_files/user_input'),
                      help='Path to user input files')
    parser.add_argument('--medication-mapping', default=str(SCRIPT_DIR / 'auxillary_files/medication_mapping_files'),
                      help='Path to medication mapping files')
    
    return parser.parse_args()

def get_source_path(args, source_name):
    """Get the source path, using individual override if specified, otherwise using source-dir."""
    individual_path = getattr(args, f'{source_name}_source', None)
    if individual_path:
        return str(Path(individual_path))
    return str(Path(args.source_dir) / source_name)

def main():
    args = parse_args()
    
    # Create paths dictionary
    pth_dic = {
        "data_path": str(Path(args.data_path)),
        "mimic4_source_path": get_source_path(args, 'mimic4'),
        "mimic3_source_path": get_source_path(args, 'mimic3'),
        "eicu_source_path": get_source_path(args, 'eicu'),
        "amsterdam_source_path": get_source_path(args, 'amsterdam'),
        "hirid_source_path": get_source_path(args, 'hirid'),
        "auxillary_files": str(Path(args.auxillary_files)),
        "vocabulary": str(Path(args.vocabulary)),
        "user_input": str(Path(args.user_input)),
        "medication_mapping_files": str(Path(args.medication_mapping))
    }
    
    # Convert paths to parquet
    omop_parquet.convert_to_parquet(pth_dic)
    
    # Generate medication mappings
    om = OMOP_Medications(pth_dic)
    ingredient_to_drug = om.run()
    
    mm = MedicationMapping(pth_dic,
                          datasets=['hirid', 
                                  'amsterdam',
                                  'mimic4',
                                  'mimic3',
                                  'eicu'])
    
    medication_json = mm.run(load_drugnames=False, fname='medications.json')
    
    # Generate diagnoses mappings
    dm = DiagnosesMapping(pth_dic, datasets=['mimic4'])

if __name__ == '__main__':
    main()
