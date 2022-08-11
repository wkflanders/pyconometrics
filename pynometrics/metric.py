import numpy as np
import pandas as pd

default_period = 50

def volatility(x, **kwargs):

    # Generates the volatility

    # x: Dataframe
    # inputcol (str): Column from x that is being used to calculate the moving average
    #                 Defaults to "Adj Close"
    # outputcol (str): Column where the moving average is being returned to
    #                 Defaults to "Sma_(period)"
    # period (int): Lookback period (in days) for calculating the average
    #                 Defaults to 50

    # Example: 
    # NDAQ_volatility = volatility(NASDAQ, period = 30)
    # AAPL = volatility(AAPL, inputcol = "Close", outputcol = "SMA")

    v = pd.DataFrame()

    period = kwargs.get("period", default_period)

    if(x.shape[1] > 1):
        _inputcol = kwargs.get("inputcol", "Adj Close")
        _x = x.loc[:, _inputcol]

        _outputcol = kwargs.get("outputcol", "Volatility")
        v[_outputcol] = _x.rolling(window=period).std()
        v = v.iloc[period: , :]

        return v
    elif(x.shape[1] < 1 ):
        raise Exception("Number of columns cannot be less than 1")
    else:
        _outputcol = kwargs.get("outputcol", "Volatility")
        v[_outputcol] = x.rolling(window=period).std()
        v = v.iloc[period: , :]

        return v

def growth(x, **kwargs):

    # Returns the 

    # x: Dataframe
    # inputcol (str): Column from x that is being used to calculate the moving average
    #                 Defaults to "Adj Close"
    # outputcol (str): Column where the moving average is being returned to
    #                 Defaults to "Sma_(period)"
    # 

    # 

    growth = pd.DataFrame()

    period = kwargs.get("period", default_period)

    if(x.shape[1] > 1):
        _inputcol = kwargs.get("inputcol", "Adj Close")
        _x = x.loc[:, _inputcol]

        _outputcol = kwargs.get("outputcol", "Volatility")
        growth[_outputcol] = _x.rolling(window=period).std()
        growth = growth.iloc[period: , :]

        return v
    elif(x.shape[1] < 1 ):
        raise Exception("Number of columns cannot be less than 1")
    else:
        _outputcol = kwargs.get("outputcol", "Volatility")
        v[_outputcol] = x.rolling(window=period).std()
        v = v.iloc[period: , :]

        return v