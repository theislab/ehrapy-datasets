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
import yaml

from blended_preprocessing.flat_and_labels import blended_FLProcessor
from blended_preprocessing.diagnoses import blended_DiagProcessor

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent.absolute()

ALL_DATASETS = ['mimic4', 'mimic3', 'hirid', 'amsterdam', 'eicu']


def parse_args():
    parser = argparse.ArgumentParser(description='Harmonize BlendedICU labels')
    parser.add_argument('--pipe', action='store_true', help='Run in pipeline mode (load all config from paths.yaml)')
    parser.add_argument('--config', default=str(SCRIPT_DIR / 'paths.yaml'), help='Path to paths.yaml')
    parser.add_argument('--datasets', type=str, help='Comma separated list of datasets to blend')
    return parser.parse_args()


def get_selected_datasets_from_yaml(paths_path):
    if Path(paths_path).is_file():
        with open(paths_path, 'r') as f:
            config = yaml.safe_load(f)
        selected = config.get('selected_datasets', None)
        if selected:
            return [d for d in selected if d in ALL_DATASETS]
    return ALL_DATASETS


def main():
    args = parse_args()
    if args.pipe:
        print("[INFO] Running in pipeline mode: loading all paths from paths.yaml in script directory")
        paths_path = SCRIPT_DIR / 'paths.yaml'
        with open(paths_path, 'r') as f:
            paths_dic = yaml.safe_load(f)
        selected_datasets = get_selected_datasets_from_yaml(paths_path)
        flp = blended_FLProcessor(datasets=selected_datasets, pth_dic=paths_dic)
        flp.run_flat_and_labels()
        dp = blended_DiagProcessor(datasets=selected_datasets, pth_dic=paths_dic)
        dp.run()
    else:
        print("[INFO] Running in standalone mode: using command-line arguments and defaults")
        if args.datasets:
            selected_datasets = [d.strip() for d in args.datasets.split(',') if d.strip() in ALL_DATASETS]
            if not selected_datasets:
                selected_datasets = ALL_DATASETS
        else:
            selected_datasets = get_selected_datasets_from_yaml(args.config)
        flp = blended_FLProcessor(datasets=selected_datasets)
        flp.run_flat_and_labels()
        dp = blended_DiagProcessor(datasets=selected_datasets)
        dp.run()


if __name__ == "__main__":
    main()
