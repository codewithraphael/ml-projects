from hypothesis import target
import pandas as pd

from config import TARGET_COLUMN, TEST_SIZE

def clean_data(data):

    '''Cleans the stock price data by removing duplicates, sorting by index, dropping missing values, and filtering out non-positive close prices.'''

    data = data.copy()
    data = data[~data.index.duplicated(keep='first')]
    data = data.sort_index()
    data = data.dropna(subset=['close'])
    data = data[data['close'] > 0]

    return data


def select_target(data, target_column=TARGET_COLUMN):

    series = data[target_column].copy()
    series.name = target_column

    return series 


def split_time_series(series, test_size=TEST_SIZE):

    '''
    split timeseries chronologically into training and testing datasets
    ''' 

    split_index = int(len(series) * 1 - test_size)

    train = series.iloc[:split_index]
    test = series.iloc[split_index:]

    print(f'\nTRAIN SIZE: \n{len(train)}')
    print(f'\nTEST SIZE: \n{len(test)}')

    return train, test
