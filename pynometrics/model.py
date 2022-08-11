import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import data

class LinearRegression:

    # Generates a linear regression for a set of data
        
    # x (ndarray): Independent variables
    # y (ndarray): Depdent variable
    # regularlization: Tuning value for regularlization of regression

    # Usage:
    # regress = LinearRegression(x, y, 0) #Instantiation
    # regress.fit() #Fitting the regression
    # y = regress.predict(x)  #Uses model to predict features 
    # err = regress.error() #Returns the mean squared error 

    # Instance attributes:
    # .m (ndarray): Returns the beta coefficients (slope)
    # .c (float): Returns the intercept

    

    def __init__(self, x, y, regularlization = 0):
        self.x = x
        self.y = y
        self.regularlization = regularlization

    def fit(self):

        X0 = np.ones((self.x.shape[0],1))

        A = np.hstack((self.x, X0))

        if(len(A.shape) > 1):
            n_col = A.shape[1]
        else:
            n_col = 1
       
        #regress = np.linalg.lstsq(A, self.y, rcond = None)[0]
        regress = np.linalg.lstsq(A.T.dot(A) + self.regularlization * np.identity(n_col), A.T.dot(self.y), rcond=None)[0]

        i = len(regress)

        self.c = regress[i-1]
        self.m = regress[:i-1]

        return self.m, self.c

    
    def error(self, features):
        try:
            MSE = np.square(np.subtract(features, self.w)).mean()
            return MSE
        except ValueError:
            raise ModelError("Mismatch dimensions between features and predicted features!")
        except AttributeError:
            raise ModelError("No fit or prediction for error to be calculated!")

    
    def predict(self, x):
        self.w = 0
        try:
            for i in range(len(self.m)):
                self.w = self.w + self.m[i]*x[:,i]               # range(len()) bad syntax but only way I can think of                                
            self.w = self.w + self.c                    # to grab index so that can be used for both m and x
            self.w = self.w.reshape(self.w.shape[0],1)
            return self.w  
        except:
            raise ModelError("No fit for prediction!")
            
class LogisticRegression:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def fit(self):
        
        return self.m, self.c


class ModelError(Exception):
    pass



x = np.array([0,1,2,3,4,5])
y = np.array([2,3,4,5,6,7])
z = np.array([0,0,1,2,4,1])
b = np.array([1,2])

x = x.reshape(x.shape[0], 1)
y = y.reshape(y.shape[0], 1)
z = z.reshape(z.shape[0], 1)
regressor = LinearRegression(x, y)
regressor.fit()
y1 = regressor.predict(z)
err = regressor.error(y)
#print(regressor.m, regressor.c)
print(y1)
print(err)

plt.plot(z, y, '.')
plt.plot(z, y1, 'r-')
plt.show()

