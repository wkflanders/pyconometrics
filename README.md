# Pyconometrics

A small and simple Python library equipped with tools for finance and econometrics.

## Installation

To install the library using pip:
```
pip install pyconometrics
```

To use, simply import the library:
```
import pyconometrics as pn
```

## Documentation

The library contains various tools for data retrieval, anaylsis, and prediction.

### Data:
The data module focuses on data collection and manipulation.
```
pn.data.history()     #Retrieves the High, Low, Open, Close, Volume, Adj Close for a security
pn.data.center()      #Centers the data around the mean
pn.data.normalize()   #Normalizes the data
```

### Moving Average:
The moving average (ma) module focuses on creating moving averages.
```
pn.ma.sma()       #Creates a simple moving average across a period
pn.ma.ema()       #Creates an exponential moving average across a period
pn.ma.macd()      #Creates the MACD line
pn.ma.bollinger() #Creates bollinger bands
```

### Metric:
The metric module contains tools to help with data anylsis.
```
pn.metric.volatility()    #Returns the historical volatility across a period
```

### Model:
The model module contains tools for creating models to help forecast and examine correlation.
```
reg = pn.model.LinearRegression()   #The linear regression class contains methods for analysis of the linear fit between a set of observations and features.
reg.fit()                           #Fits the data
reg.predict()                       #Creates a prediction based on a defined fit
reg.error()                         #Returns the Mean Squared Error for the prediction
reg.m                               #Returns the slope m for the prediction
reg.c                               #Returns the y-intercept c for the prediction
```

## Final Notes
This project is very much still in development. Econometrics and finance are topics that are endlessly interesting as well as computer science and programming. There is always more to be added, learned, and improved upon. I'm excited to see where this project goes.

