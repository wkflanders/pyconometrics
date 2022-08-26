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
            _x = _x.iloc[:,-period]

            _outputcol = kwargs.get("outputcol", volstring)
            v[_outputcol] = _x.rolling(window=period).std().dropna(axis="index")*np.sqrt(period)

            return v
        else:
            x = x.iloc[:,-period]

            _outputcol = kwargs.get("outputcol", volstring)
            v[_outputcol] = x.rolling(window=period).std().dropna(axis="index")*np.sqrt(period)

            return v
    else:
        raise ValueError("Input must be a dataframe!")



#WIP
# def growth(x, initial, end, **kwargs):

#     # Returns the growth

#     # x: Dataframe
#     # inputcol (str): Column from x that is being used to calculate the growth
#     #                 Defaults to "Adj Close"
#     # outputcol (str): Column where the growth is being returned to
#     #                  Defaults to "Growth_(period)"
#     # initial (str): Initial date from which to calculate growth
#     #                In YYYY-MM-DD format
#     # end (str): End date from which to calculate growth
#     #            In YYYY-MM-DD format

#     try:
#         datetime.datetime.strptime(initial, '%Y-%m-%d')
#         datetime.datetime.strptime(end, '%Y-%m-%d')
#     except ValueError:
#         raise ValueError("Initial and end dates must be in YYYY-MM-DD format!")

#     growth = pd.DataFrame()

#     period = kwargs.get("period", default_period)

#     is_df = isinstance(pd.DataFrame)

#     if(is_df):
#         if(x.shape[1] < 1):
#             raise IndexError("Number of columns must be greater than 1!")
#         elif(x.shape[1] > 1):
#             _inputcol = kwargs.get("inputcol", "Adj Close")
#             _x = x[[_inputcol]]
#             indx = _x.loc(_x['Date'].values == initial)
