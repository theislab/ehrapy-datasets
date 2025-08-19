import sys
import pandas as pd
import pyarrow.parquet as pq

def describe_parquet(file_path):
    try:
        df = pd.read_parquet(file_path)
        print("Column names:", df.columns.tolist())
        print("Number of rows:", len(df))
        return
    except Exception as e:
        print(f"Warning: Could not fully read with Pandas: {e}")
        print("Falling back to PyArrow metadata...")

    try:
        parquet_file = pq.ParquetFile(file_path)
        schema = parquet_file.schema
        num_rows = parquet_file.metadata.num_rows

        print("Column names:", schema.names)
        print("Number of rows:", num_rows)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e2:
        print(f"Error reading '{file_path}' metadata: {e2}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python results.py <parquet_file>")
        sys.exit(1)
    describe_parquet(sys.argv[1])
