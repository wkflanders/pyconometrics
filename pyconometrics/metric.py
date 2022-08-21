import numpy as np
import pandas as pd

default_period = 50

def volatility(x, **kwargs):

    # Generates the trailing volatility

    # x: Dataframe
    # inputcol (str): Column from x that is being used to calculate the volatility
    #                 Defaults to "Adj Close"
    # outputcol (str): Column where the volatility is being returned to
    #                 Defaults to "Volatility_(period)"
    # period (int): Lookback period (in days) that volatility is being calculated across
    #                 Defaults to 50 days

    # Example: 
    # NDAQ_volatility = volatility(NASDAQ, period = 30)
    # AAPL = volatility(AAPL, inputcol = "Close", outputcol = "SMA")

    v = pd.DataFrame()

    period = kwargs.get("period", default_period)
    volstring = "Volatility_"+str(period)

    is_df = isinstance(x, pd.DataFrame)

    if(is_df):
        if(x.shape[1] < 1):
            raise IndexError("Number of columns must be greater than 1!")
        elif(x.shape[1] > 1):
            _inputcol = kwargs.get("inputcol", "Adj Close")
            _x = x[[_inputcol]]

            _outputcol = kwargs.get("outputcol", volstring)
            v[_outputcol] = _x.rolling(window=period).std().dropna(axis="index")*np.sqrt(period)

            return v
        else:
            _outputcol = kwargs.get("outputcol", volstring)
            v[_outputcol] = x.rolling(window=period).std().dropna(axis="index")*np.sqrt(period)

            return v
    else:
        raise ValueError("Input must be a dataframe!")


def growth(x, **kwargs):

    # Returns the growth

    # x: Dataframe
    # inputcol (str): Column from x that is being used to calculate the growth
    #                 Defaults to "Adj Close"
    # outputcol (str): Column where the growth is being returned to
    #                 Defaults to "Growth_(period)"
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
