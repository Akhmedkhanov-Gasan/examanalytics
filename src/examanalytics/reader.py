import csv
from pathlib import Path


def read_csv_files(file_paths: list[str]):
    """
    Read multiple CSV files and return all rows as list of dicts.
    """
    all_rows: list[dict[str, str]] = []

    for file_path in file_paths:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        with path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            all_rows.extend(reader)

    return all_rows
