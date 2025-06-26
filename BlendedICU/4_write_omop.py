"""
At this point, the dataset is ready to be written to the OMOP format.
Most tables are very quickly written. Only the drug_exposure and measurement 
variables require a lot of time. 
"""
import argparse
import yaml

from blended_preprocessing.omop_conversion import OMOP_converter

# Get the directory where this script is located
from pathlib import Path
SCRIPT_DIR = Path(__file__).parent.absolute()

def parse_args():
    parser = argparse.ArgumentParser(description='Write OMOP tables from blendedICU data')
    parser.add_argument('--pipe', action='store_true', help='Run in pipeline mode (load all config from paths.yaml)')
    parser.add_argument('--paths', default=str(SCRIPT_DIR / 'paths.yaml'), help='Path to paths.yaml')
    # Optionally add more args for manual mode if needed
    return parser.parse_args()


def main():
    args = parse_args()
    if args.pipe:
        print("[INFO] Running in pipeline mode: loading all config from paths.yaml in script directory")
        with open(args.paths, 'r') as f:
            paths_dic = yaml.safe_load(f)
        # Inject pth_dic from paths.yaml
        omop = OMOP_converter(initialize_tables=True, pth_dic=paths_dic)
    else:
        print("[INFO] Running in standalone mode: using command-line arguments and defaults")
        omop = OMOP_converter(initialize_tables=True, pth_dic=None, config_path=None)

    omop.observation_period_table()
    omop.measurement_table()
    omop.drug_exposure_table()

if __name__ == "__main__":
    main()

