"""
This script lauches the timeseriesprocessing (tsp) and the flat and labels 
processing (flp) for the mimic database. 
Note that this produces the 'raw' data of the BlendedICU dataset.
The preprocessed BlendedICU dataset will then be obtained with 3_blendedICU.py
Approximate running time: <1min.
"""
import argparse
from pathlib import Path

from mimic4_preprocessing.flat_and_labels import mimic4_FLProcessor
from mimic4_preprocessing.diagnoses import mimic4_DiagProcessor
from mimic4_preprocessing.timeseries import mimic4TSP

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent.absolute()

def parse_args():
    parser = argparse.ArgumentParser(description='Harmonize MIMIC4 data')
    
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
    data_dir = Path(args.data_path) / 'mimic4_data'
    pth_dic = {
        "data_path": str(Path(args.data_path)),
        "savepath": str(data_dir / ''),
        "labels_savepath": str(data_dir / 'labels.parquet'),
        "flat_savepath": str(data_dir / 'flat.parquet'),
        "diag_savepath": str(data_dir / 'diagnoses.parquet'),
        "auxillary_files": str(Path(args.auxillary_files)),
        "user_input": str(Path(args.user_input)),
        "vocabulary": str(Path(args.auxillary_files) / 'OMOP_vocabulary'),
        "medication_mapping_files": str(Path(args.auxillary_files) / 'medication_mapping_files'),
        "user_input_pth": str(Path(args.user_input) / ''),
        "dir_long_timeseries": str(Path(args.data_path) / 'blended_data/formatted_timeseries'),
        "dir_long_medication": str(Path(args.data_path) / 'blended_data/formatted_medications'),
        "partiallyprocessed_ts_dir": str(Path(args.data_path) / 'blended_data/partially_processed_timeseries'),
        "preprocessed_diagnoses_pth": str(Path(args.data_path) / 'blended_data/preprocessed_diagnoses.parquet')
    }
    
    tsp = mimic4TSP(
        med_pth='medication.parquet',
        ts_pth='timeseries.parquet',
        tslab_pth='timeserieslab.parquet',
        outputevents_pth='timeseriesoutputs.parquet',
        pth_dic=pth_dic,
        config_path=args.config)

    tsp.run_harmonization()

    flp = mimic4_FLProcessor(pth_dic=pth_dic, config_path=args.config)

    flp.run_labels()

    dp = mimic4_DiagProcessor(pth_dic=pth_dic, config_path=args.config)

    dp.run()


if __name__ == "__main__":
    main()
