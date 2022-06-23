# -*- coding: utf-8 -*-
"""DataminingLAB3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sZ1gBeWY3CbgrKSOwxXTMgldSmcu1e6g
"""

from google.colab import drive 
drive.mount('/content/drive')
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('/content/drive/MyDrive/Data mining/FuelConsumption.csv')
df

df.shape

df.isnull()

x=df[["ENGINESIZE"]].values
y=df["CO2EMISSIONS"]



from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.25,random_state=1)



from sklearn.linear_model import LinearRegression

reg=LinearRegression()

reg.fit(x_train, y_train)

reg.predict(x_test)

reg.score(x_test,y_test)

reg.coef_

reg.intercept_