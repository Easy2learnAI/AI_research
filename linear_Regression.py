# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 16:35:12 2022

@author: Mohamed Fortas
"""

from sklearn.linear_model import LinearRegression \
from sklearn.svm import SVR
import numpy as np
import matplotlib.pyplot as plt

model = LinearRegression()
#model = SVR(C= 100)

x = np.linspace(0, 10, 100).reshape(100, 1)
X = np.linspace(0, 10, 100).reshape(100, 1)
y= x + np.random.randn(100, 1)
#y= x**2 + np.random.randn(100, 1)

model.fit(x,y)

model.score(x, y)

P = model.predict(X)

plt.scatter(x, y)
plt.plot(X, P, c = 'r')


                                                