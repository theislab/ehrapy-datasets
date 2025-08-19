import gzip
import os
import pandas as pd

def compress_csv_files_in_folder(folder_path):
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            # Open the original .csv file
            csv_file_path = os.path.join(folder_path, filename)
            with open(csv_file_path, 'rb') as csv_file:
                # Create a .csv.gz file
                gz_file_path = csv_file_path + '.gz'
                with gzip.open(gz_file_path, 'wb') as gz_file:
                    gz_file.writelines(csv_file)

            print(f"Compressed: {gz_file_path}")

# Specify the folder path containing your .csv files
#folder_path = '/home/andreas/Helmholtz/ehrapy-datasets/BlendedICU/source/mimic4/hosp/'
#compress_csv_files_in_folder(folder_path)

def read_one_column_from_csv(file_path, column_name):
    with gzip.open(file_path, 'rt', encoding='utf-8', errors='replace') as f:
        df = pd.read_csv(f, usecols=[column_name])
    return df[column_name].dropna().tolist()

file_path = 'source/mimic4large/hosp/prescriptions.csv.gz'
column_name = 'form_rx'
data = read_one_column_from_csv(file_path, column_name)
print(data)