import pandas as pd
import pandas_datareader as web
import numpy as np

import datetime as dt

default_start = dt.datetime(2001,1,1)
default_end = dt.datetime.now()

def history(ticker, start = default_start, end = default_end):
    
    df = web.DataReader(ticker, "yahoo", start = start, end = end)
    return df



def preprocess(func):
    def process(x, *args, **kwargs):
        _x = x

        is_df = isinstance(_x, pd.DataFrame)
        _data = (_x.values if is_df else _x)
        
        processed_data = func(_data)

        process_df = pd.DataFrame(processed_data, index=_x.index, columns = _x.columns)

        return process_df

    return process


@preprocess
def center(x):
    
    adjustment = np.mean(x, axis=0).reshape(1, x.shape[1])
    centered = x - adjustment
    
    return centered


@preprocess
def normalize(x):

    center_x = center(x)
    adjustment = np.std(center_x, axis=0).reshape(1, center_x.shape[1])
    normal = center_x / adjustment
    
    return normal


#Do transform function
#def transform(x):

