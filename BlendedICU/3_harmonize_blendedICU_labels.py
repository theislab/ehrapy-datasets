"""
Processing of the BlendedICU dataset. 
The raw timeseries data of the blendedICU dataset is already computed at step 2
Only the labels processing needs to be done to get the complete raw dataset.

blendedicuTSP creates the processed blendedICU dataset by adding resampling, 
missing values imputation and clipping&normalization steps. All these steps 
are optional and customizable using the config.json file.
"""
import argparse
from pathlib import Path

from blended_preprocessing.flat_and_labels import blended_FLProcessor
from blended_preprocessing.diagnoses import blended_DiagProcessor

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent.absolute()

def parse_args():
    parser = argparse.ArgumentParser(description='Harmonize BlendedICU labels')
    
    # Required paths
    parser.add_argument('--data-path', default=str(SCRIPT_DIR / 'data'),
                      help='Path to store processed data')
    
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
        "auxillary_files": str(Path(args.auxillary_files)),
        "user_input": str(Path(args.user_input)),
        "vocabulary": str(Path(args.auxillary_files) / 'OMOP_vocabulary'),
        "medication_mapping_files": str(Path(args.auxillary_files) / 'medication_mapping_files')
    }
    
    flp = blended_FLProcessor(datasets=['mimic4',
                                        'mimic3',
                                        'hirid',
                                        'amsterdam',
                                        'eicu'],
                              pth_dic=pth_dic,
                              config_path=args.config)
    flp.run_flat_and_labels()

    dp = blended_DiagProcessor(datasets=['mimic4'],
                               pth_dic=pth_dic,
                               config_path=args.config)

    dp.run()


if __name__ == "__main__":
    main()
