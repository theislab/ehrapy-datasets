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
    parser.add_argument('--pipe', action='store_true', help='If set, load all config from paths.yaml and ignore other args')
    parser.add_argument('--data-path', help='Path to store processed data')
    parser.add_argument('--auxillary-files', help='Path to auxillary files')
    parser.add_argument('--user-input', help='Path to user input files')
    parser.add_argument('--config', default='config.json', help='Path to config file')
    return parser.parse_args()


def main():
    args = parse_args()
    if args.pipe:
        print("[INFO] Running in pipeline mode: loading all config from paths.yaml in script directory")
        import yaml
        with open('paths.yaml', 'r') as f:
            paths = yaml.safe_load(f)
        data_path = paths.get('data_dir')
        auxillary_files = paths.get('auxillary_files')
        user_input = paths.get('user_input_dir')
        config_path = 'config.json'
    else:
        print("[INFO] Running in standalone mode: using command-line arguments and defaults")
        data_path = args.data_path or str(SCRIPT_DIR / 'data')
        auxillary_files = args.auxillary_files or str(SCRIPT_DIR / 'auxillary_files')
        user_input = args.user_input or str(SCRIPT_DIR / 'auxillary_files/user_input')
        config_path = args.config

    # Create paths dictionary
    data_dir = Path(data_path) / 'mimic4_data'
    pth_dic = {
        "data_path": str(Path(data_path)),
        "savepath": str(data_dir),
        "labels_savepath": str(data_dir / 'labels.parquet'),
        "flat_savepath": str(data_dir / 'flat.parquet'),
        "diag_savepath": str(data_dir / 'diagnoses.parquet'),
        "auxillary_files": str(Path(auxillary_files)),
        "user_input": str(Path(user_input)),
        "vocabulary": str(Path(auxillary_files) / 'OMOP_vocabulary'),
        "medication_mapping_files": str(Path(auxillary_files) / 'medication_mapping_files'),
        "user_input_pth": str(Path(user_input)),
        "dir_long_timeseries": str(Path(data_path) / 'blended_data' / 'formatted_timeseries'),
        "dir_long_medication": str(Path(data_path) / 'blended_data' / 'formatted_medications'),
        "partiallyprocessed_ts_dir": str(Path(data_path) / 'blended_data' / 'partially_processed_timeseries'),
        "preprocessed_diagnoses_pth": str(Path(data_path) / 'blended_data' / 'preprocessed_diagnoses.parquet')
    }

    tsp = mimic4TSP(
        med_pth='medication.parquet',
        ts_pth='timeseries.parquet',
        tslab_pth='timeserieslab.parquet',
        outputevents_pth='timeseriesoutputs.parquet',
        pth_dic=pth_dic,
        config_path=config_path)

    tsp.run_harmonization()

    flp = mimic4_FLProcessor(pth_dic=pth_dic, config_path=config_path)

    flp.run_labels()

    dp = mimic4_DiagProcessor(pth_dic=pth_dic, config_path=config_path)

    dp.run()


if __name__ == "__main__":
    main()
