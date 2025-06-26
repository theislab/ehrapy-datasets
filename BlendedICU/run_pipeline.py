import argparse
import subprocess
import sys
from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler
import yaml
import os

PIPELINE_STEPS = [
    ("mimic3", "1_extract_mimic3.py", "2_harmonize_mimic3.py"),
    ("mimic4", "1_extract_mimic4.py", "2_harmonize_mimic4.py"),
    ("hirid", "1_extract_hirid.py", "2_harmonize_hirid.py"),
    ("eicu", "1_extract_eicu.py", "2_harmonize_eicu.py"),
    ("amsterdam", "1_extract_amsterdam.py", "2_harmonize_amsterdam.py"),
]

DATASET_PATH_KEYS = {
    "mimic3": "mimic3_source",
    "mimic4": "mimic4_source",
    "hirid": "hirid_source",
    "eicu": "eicu_source",
    "amsterdam": "amsterdam_source",
}

AUX_KEYS = {
    "auxillary_files": "auxillary_files",
    "user_input_dir": "user_input_dir",
    "omop_vocabulary_dir": "omop_vocabulary_dir",
    "medication_mapping_dir": "medication_mapping_dir"
}

LOG_FILE = Path(__file__).parent / "pipeline.log"


def setup_logger():
    logger = logging.getLogger("pipeline")
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(LOG_FILE, maxBytes=5*1024*1024, backupCount=2)
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def print_and_log(logger, level, message):
    print(message)
    if level == 'info':
        logger.info(message)
    elif level == 'warning':
        logger.warning(message)
    elif level == 'error':
        logger.error(message)


def prompt_select_datasets():
    print("Select datasets to blend (comma separated, e.g. mimic3,mimic4), or type 'all' for all datasets:")
    print("Available: mimic3, mimic4, hirid, eicu, amsterdam")
    while True:
        inp = input("Datasets: ").strip().lower()
        if inp == 'all':
            return list(DATASET_PATH_KEYS.keys())
        if not inp:
            print("Please enter at least one dataset or 'all'.")
            continue
        selected = [d.strip() for d in inp.split(",") if d.strip() in DATASET_PATH_KEYS]
        if selected:
            return selected
        print("Invalid selection. Try again.")


def prompt_customize_paths():
    while True:
        inp = input("Do you want to customize any of the paths? [y/N]: ").strip().lower()
        if inp in ('y', 'yes'):
            return True
        if inp in ('n', 'no', ''):
            return False
        print("Please enter 'y' or 'n'.")


def prompt_dataset_path(dataset, default):
    while True:
        inp = input(f"Path for {dataset} [{default}]: ").strip()
        if not inp:
            inp = default
        if os.path.exists(inp):
            return inp
        print(f"Warning: Path '{inp}' does not exist.")
        print("Options: [I]gnore this dataset, [C]hange path, [Q]uit pipeline")
        opt = input("Your choice (I/C/Q): ").strip().lower()
        if opt == "i":
            return None
        elif opt == "c":
            continue
        elif opt == "q":
            print("Pipeline cancelled.")
            sys.exit(1)
        else:
            print("Invalid option.")


def prompt_processed_data_dir(default):
    while True:
        inp = input(f"Directory to store processed data [{default}]: ").strip()
        if not inp:
            inp = default
        # Accept any path, create if needed
        return inp


def prompt_auxillary_files(default):
    while True:
        inp = input(f"Path for auxillary files [{default}]: ").strip()
        if not inp:
            inp = default
        if os.path.exists(inp):
            return inp
        print(f"Warning: Path '{inp}' does not exist.")
        print("Options: [C]hange path, [Q]uit pipeline")
        opt = input("Your choice (C/Q): ").strip().lower()
        if opt == "c":
            continue
        elif opt == "q":
            print("Pipeline cancelled.")
            sys.exit(1)
        else:
            print("Invalid option.")


def update_config_yaml(config_path, selected_datasets, dataset_paths, aux_paths):
    # Load existing config if present
    config = {}
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            config = yaml.safe_load(f) or {}

    # Build new config, sorted and grouped
    new_config = {}
    # Source data directories
    for ds in DATASET_PATH_KEYS:
        new_config[DATASET_PATH_KEYS[ds]] = dataset_paths.get(ds, config.get(DATASET_PATH_KEYS[ds], f"source/{ds}/"))
    # Output data directories
    data_dir_value = config.get("data_dir", "data/")
    new_config["data_dir"] = data_dir_value
    new_config["data_path"] = data_dir_value
    for ds in DATASET_PATH_KEYS:
        new_config[f"{ds}_data"] = config.get(f"{ds}_data", f"data/{ds}_data/")
    # Auxiliary files
    for k, key in AUX_KEYS.items():
        new_config[key] = aux_paths.get(key, config.get(key, f"auxillary_files/{key.split('_')[0]}/"))
    # Add legacy keys for compatibility
    new_config["vocabulary"] = new_config["omop_vocabulary_dir"]
    new_config["user_input"] = new_config["user_input_dir"]
    new_config["medication_mapping_files"] = new_config["medication_mapping_dir"]
    new_config["diagnoses_json"] = config.get("diagnoses_json", "auxillary_files/diagnoses.json")
    new_config["medications_v11_json"] = config.get("medications_v11_json", "auxillary_files/medications_v11.json")
    # Harmonized output
    new_config["dataset_harmonized"] = config.get("dataset_harmonized", "data/blendedICU_harmonized/")
    # OMOP output directory
    new_config["omop_output"] = config.get("omop_output", "data/omop/")
    # Selected datasets
    new_config["selected_datasets"] = selected_datasets
    # Write config
    with open(config_path, "w") as f:
        yaml.safe_dump(new_config, f, sort_keys=False)


def run_step(script, paths_path, logger, config_path=None):
    print_and_log(logger, 'info', f"INFO: Running step: {script}")
    script_path = Path(__file__).parent / script
    # Only pass --pipe to signal pipeline mode; scripts will use default config file locations
    cmd = [sys.executable, str(script_path), "--pipe"]
    def print_important_lines(text):
        if not text:
            return
        for line in text.splitlines():
            if (line.startswith("INFO") or line.startswith("ERROR") or line.startswith("WARNING")):
                print(line)
    try:
        result = subprocess.run(cmd, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print_and_log(logger, 'error', f"ERROR: Step failed: {script}")
        print("See pipeline.log for error details and traceback.")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Run the full BlendedICU pipeline.")
    parser.add_argument("--paths", type=str, default="paths.yaml", help="Path to paths.yaml (for path-based scripts)")
    parser.add_argument("--config", type=str, default="config.json", help="Path to config.json (for extract/harmonize steps)")
    parser.add_argument("--datasets", type=str, help="Comma separated list of datasets to blend")
    for ds in DATASET_PATH_KEYS:
        parser.add_argument(f"--{ds}-path", type=str, help=f"Path to {ds} dataset")
    parser.add_argument("--auxillary-files", type=str, help="Path to auxillary files")
    parser.add_argument("--from-step", type=int, default=0, help="Start from this step index (0-based)")
    parser.add_argument("--to-step", type=int, default=None, help="End at this step index (inclusive)")
    args = parser.parse_args()

    logger = setup_logger()
    print_and_log(logger, 'info', f"INFO: Pipeline started with config: {args.paths}")

    # Dataset selection FIRST
    if args.datasets:
        selected_datasets = [d.strip() for d in args.datasets.split(",") if d.strip() in DATASET_PATH_KEYS]
        if not selected_datasets:
            print("No valid datasets selected. Exiting.")
            sys.exit(1)
    else:
        selected_datasets = prompt_select_datasets()

    # Ask if user wants to customize paths
    customize = prompt_customize_paths()

    dataset_paths = {}
    data_dir = "data/"  # default
    aux_path = "auxillary_files/"
    if customize:
        # Prompt for each selected dataset's source path
        for ds in selected_datasets:
            default = f"source/{ds}/"
            path = prompt_dataset_path(ds, default)
            if path:
                dataset_paths[ds] = path
            else:
                print(f"{ds} will be ignored.")
        # Remove datasets with None path
        selected_datasets = [ds for ds in selected_datasets if dataset_paths.get(ds)]
        if not selected_datasets:
            print("No valid datasets selected. Exiting.")
            sys.exit(1)
        # Prompt for processed data directory
        data_dir = prompt_processed_data_dir("data/")
        # Prompt for auxillary files
        aux_path = prompt_auxillary_files("auxillary_files/")
    else:
        # Use defaults or command-line args
        for ds in selected_datasets:
            arg_path = getattr(args, f"{ds}_path")
            if arg_path:
                dataset_paths[ds] = arg_path
            else:
                dataset_paths[ds] = f"source/{ds}/"
        data_dir = "data/"
        aux_path = args.auxillary_files or "auxillary_files/"

    aux_paths = {
        "auxillary_files": aux_path,
        "user_input_dir": os.path.join(aux_path, "user_input"),
        "omop_vocabulary_dir": os.path.join(aux_path, "OMOP_vocabulary"),
        "medication_mapping_dir": os.path.join(aux_path, "medication_mapping_files"),
    }

    # Update paths.yaml
    update_config_yaml(args.paths, selected_datasets, dataset_paths, aux_paths)

    # Build pipeline steps
    steps = ["0_prepare_files.py"]
    for ds, extract, harmonize in PIPELINE_STEPS:
        if ds in selected_datasets:
            steps.extend([extract, harmonize])
    steps.extend(["3_harmonize_blendedICU_labels.py", "4_write_omop.py"])

    # Step range
    from_step = args.from_step
    to_step = args.to_step if args.to_step is not None else len(steps) - 1

    for i, script in enumerate(steps):
        if i < from_step or i > to_step:
            continue
        run_step(script, args.paths, logger, config_path=args.config)
    print_and_log(logger, 'info', "INFO: Pipeline completed successfully.")

if __name__ == "__main__":
    main() 