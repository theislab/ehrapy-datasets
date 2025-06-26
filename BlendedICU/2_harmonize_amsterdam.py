"""
This script lauches the timeseriesprocessing (tsp) and the flat and labels 
processing (flp) for the amsterdam database. 
Note that this produces the 'raw' data of the BlendedICU dataset.
The preprocessed BlendedICU dataset will then be obtained with 3_blendedICU.py
Approximate running time: 2min
"""
from amsterdam_preprocessing.timeseries import amsterdamTSP
from amsterdam_preprocessing.flat_and_labels import Ams_FLProcessor
from pathlib import Path

tsp = amsterdamTSP(
    ts_pth='numericitems.parquet',
    listitems_pth='listitems.parquet',
    gcs_scores_pth='glasgow_coma_scores.parquet')

tsp.run_harmonization()

flp = Ams_FLProcessor()

flp.run_labels()

# Create paths dictionary
data_dir = Path(data_path) / 'amsterdam_data'
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
