import pandas as pd

from config import file_path

def load_data():

    filepath = file_path

    if not filepath.exists():
        raise FileExistsError(f'File Not Found {filepath}')

    data = pd.read_csv(filepath, parse_dates=[0])
    data['Date'] = pd.to_datetime(data['Date'], utc=True)
    data.set_index(['Date'], inplace=True)
    data.columns = data.columns.str.lower()

    return data