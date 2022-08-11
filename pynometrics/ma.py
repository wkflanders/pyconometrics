import pandas as pd
import numpy as np

import data

default_period = 50
default_span = 50

def sma(x, **kwargs):

    # Generates a simple moving average

    # x: Dataframe
    # inputcol (str): Column from x that is being used to calculate the moving average
    #                 Defaults to "Adj Close"
    # outputcol (str): Column where the moving average is being returned to
    #                 Defaults to "Sma_(period)"
    # period (int): Lookback period (in days) for calculating the average
    #                 Defaults to 50

    # Example: 
    # NDAQ_30ma = sma(NASDAQ, period = 30)
    # AAPL_sma = sma(AAPL, inputcol = "Close", outputcol = "SMA")
    # google = sma(GOOGL)

    
    ma = pd.DataFrame()

    period = kwargs.get("period", default_period)
    sma_string = "Sma_"+str(period)

    if(x.shape[1] > 1):
        _inputcol = kwargs.get("inputcol", "Adj Close")
        _x = x.loc[:, _inputcol]

        _outputcol = kwargs.get("outputcol", sma_string)
        ma[_outputcol] = _x.rolling(window=period).mean()
        ma = ma.iloc[period: , :]
        return ma
    elif(x.shape[1] < 1 ):
        raise Exception("Number of columns cannot be less than 1")
    else:
        _outputcol = kwargs.get("outputcol", sma_string)
        ma[_outputcol] = x.rolling(window=period).mean()
        ma = ma.iloc[period: , :]
        return ma


def ema(x, **kwargs):

    # Generates an exponential moving average

    # x: Dataframe
    # inputcol (str): Column from x that is being used to calculate the moving average
    #                 Defaults to "Adj Close"
    # outputcol (str): Column where the moving average is being returned to
    #                 Defaults to "Sma_(period)"
    # span (int): Span for the exponential function
    #                 Defaults to 50

    # Example: 
    # NDAQ_30ema = ema(NASDAQ, span = 30)
    # AAPL_ema = ema(AAPL, inputcol = "Close", outputcol = "SMA")
    # google = ema(GOOGL)


    ma = pd.DataFrame()

    _span = kwargs.get("span", default_span)
    ema_string = "Ema_"+str(_span)

    if(x.shape[1] > 1):
        _inputcol = kwargs.get("inputcol", "Adj Close")
        _x = x.loc[:, _inputcol]

        _outputcol = kwargs.get("outputcol", ema_string)
        ma[_outputcol] = _x.ewm(span=_span, adjust=True).mean()
        ma = ma.iloc[_span: , :]
        return ma
    elif(x.shape[1] < 1 ):
        raise Exception("Number of columns cannot be less than 1")
    else:
        _outputcol = kwargs.get("outputcol", ema_string)
        ma[_outputcol] = x.ewm(span=_span, adjust=True).mean()
        ma = ma.iloc[_span: , :]
        return ma


def macd(x, **kwargs):

    # Generates the moving average convergence divergence
        
    # x: Dataframe
    # inputcol (str): Column from x that is being used to calculate the MACD
    #                 Defaults to "Adj Close"
    # outputcol (str): Column where the MACD is being returned to
    #                 Defaults to "MACD"

    # Example: 
    # SP500MACD = macd(SP500)
    
    macd = pd.DataFrame()

    if(x.shape[1] > 1):

        _inputcol = kwargs.get("inputcol", "Adj Close")

        _12periodema = ema(x, span=12, inputcol = _inputcol)
        _26periodema = ema(x, span=26, inputcol = _inputcol)

        _outputcol = kwargs.get("outputcol", "MACD")
        
        macd[_outputcol] = _12periodema["Ema_12"].subtract(_26periodema["Ema_26"])
        macd["Signal Line"] = ema(macd, span=9)
        macd = macd.iloc[26: , :]

        return macd
    elif(x.shape[1] < 1 ):
        raise Exception("Number of columns cannot be less than 1")
    else:
        _outputcol = kwargs.get("outputcol", "MACD")

        _12periodema = ema(x, span=12)
        _26periodema = ema(x, span=26)

        macd[_outputcol] = _12periodema["Ema_12"].subtract(_26periodema["Ema_26"])
        macd = macd.iloc[26: , :]
        macd["Signal Line"] = ema(macd, span=9)

        return macd

#def bollinger(x, **kwargs):
    
x = np.array()
