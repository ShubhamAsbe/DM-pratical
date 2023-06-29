# -*- coding: utf-8 -*-
"""COVID ARIMA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CXhOWlFiNUKqxxnyiA8cdoBGHnH-2f17
"""

import pandas as pd
import seaborn as sns # informative statistical graphics.
import statsmodels.api as sm #for ARIMA and SARIMAX
import datetime
from datetime import timedelta

df = pd.read_csv('/content/covid_19_india.csv')

df= df.drop(labels = ["Sno","State","Time","Cured","Deaths"], axis= 1, inplace= False)

df.head()

import matplotlib.pyplot as plt
sns.lineplot(x="Date", y="Confirmed",legend = 'full' , data=df)
plt.title("Confirmed Cases Over Time")
plt.xticks(rotation=45)
plt.show()

import matplotlib.pyplot as plt
sns.lineplot(x="Date", y="Confirmed",legend = 'full' , data=df, ci=None)
plt.title("Confirmed Cases Over Time")
plt.xticks(rotation=90)
plt.show()

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

df = df.resample('W').sum()

train_data = df[:int(0.9*(len(df)))]
test_data = df[int(0.9*(len(df))):]

import statsmodels.api as sm

model = sm.tsa.arima.ARIMA(train_data, order=(2,1,2))
model_fit = model.fit()

predictions = model_fit.predict(start=len(train_data), end=len(train_data)+len(test_data)-1, typ='levels')

plt.figure(figsize=(10,6))
plt.plot(train_data, label='Training Data')
plt.plot(test_data, label='Testing Data')
plt.plot(predictions, label='Predicted Data')
plt.legend()
plt.show()