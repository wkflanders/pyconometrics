import pandas as pd
import numpy as np


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

    is_df = isinstance(x, pd.DataFrame)

    if(is_df):
        if(x.shape[1] < 1):
            raise IndexError("Number of columns must be greater than 1!")
        elif(x.shape[1] > 1):
            _inputcol = kwargs.get("inputcol", "Adj Close")
            _x = x[[_inputcol]]

            _outputcol = kwargs.get("outputcol", sma_string)
            ma[_outputcol] = _x.rolling(window=period).mean().dropna(axis="index")

            return ma 
        else:
            _outputcol = kwargs.get("outputcol", sma_string)
            ma[_outputcol] = x.rolling(window=period).mean().dropna(axis="index")

            return ma
    else:
        raise TypeError("Input must be a dataframe!")
    

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

    is_df = isinstance(x, pd.DataFrame)

    if(is_df):
        if(x.shape[1] < 1):
            raise IndexError("Number of columns must be greater than 1!")
        elif(x.shape[1] > 1):
            _inputcol = kwargs.get("inputcol", "Adj Close")
            _x = x[[_inputcol]]

            _outputcol = kwargs.get("outputcol", ema_string)
            ma[_outputcol] = _x.ewm(span=_span, adjust=True).mean().dropna(axis="index")

            return ma
        else:
            _outputcol = kwargs.get("outputcol", ema_string)
            ma[_outputcol] = x.ewm(span=_span, adjust=True).mean().dropna(axis="index")

            return ma
    else:
        raise TypeError("Input must be a dataframe!")
    

def macd(x, **kwargs):

    # Generates the moving average convergence divergence
        
    # x: Dataframe
    # inputcol (str): Column from x that is being used to calculate the MACD
    #                 Defaults to "Adj Close"

    # Example: 
    # SP500MACD = macd(SP500)
    
    macd = pd.DataFrame()

    is_df = isinstance(x, pd.DataFrame)

    if(is_df):
        if(x.shape[1] < 1):
            raise IndexError("Number of columns must be greater than 1!")
        elif(x.shape[1] > 1):

            _inputcol = kwargs.get("inputcol", "Adj Close")

            _12periodema = ema(x, span=12, inputcol = _inputcol)
            _26periodema = ema(x, span=26, inputcol = _inputcol)
            
            macd["MACD"] = _12periodema["Ema_12"].subtract(_26periodema["Ema_26"]).dropna(axis="index")
            macd["Signal Line"] = ema(macd, span=9).dropna(axis="index")

            return macd
        else:
            _12periodema = ema(x, span=12)
            _26periodema = ema(x, span=26)

            macd["MACD"] = _12periodema["Ema_12"].subtract(_26periodema["Ema_26"]).dropna(axis="index")
            macd["Signal Line"] = ema(macd, span=9).dropna(axis="index")

            return macd
    else:
        raise TypeError("Input must be a dataframe!")
   

def bollinger(x, **kwargs):
    
    # Generates bollinger bands
        
    # x: Dataframe
    # inputcol (str): Column from x that is being used to calculate the MACD
    #                 Defaults to "Adj Close"
    # period (int): Lookback period (in days) for calculating the average
    #                 Defaults to 20

    # Example: 
    # SP500MACD = macd(SP500)

    boll = pd.DataFrame()

    _period = kwargs.get("period", 20)

    is_df = isinstance(x, pd.DataFrame)

    if(is_df):
        if(x.shape[1] < 1):
            raise IndexError("Number of columns must be greater than 1!")
        elif(x.shape[1] > 1):
            _inputcol = kwargs.get("inputcol", "Adj Close")
            _x = x[[_inputcol]]

            std = _x.rolling(window=_period).std().dropna(axis="index")

            simplema = _x.rolling(window=_period).mean().dropna(axis="index")

            boll["Upper Band"] = simplema + std*2
            boll["Lower Band"] = simplema - std*2 

            return boll
        else:
            std = x.rolling(window=_period).std().dropna(axis="index")

            simplema = x.rolling(window=_period).mean().dropna(axis="index")

            boll["Upper Band"] = simplema.add(std*2)
            boll["Lower Band"] = simplema.subtract(std*2)

            return boll
    else:
        return ValueError("Input must be a dataframe!")
