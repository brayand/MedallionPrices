# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 07:50:25 2015
http://chicagodispatcher.com/chicago-taxicab-medallion-prices-p235-117.htm
@author: abray
"""
import datetime as dt
import numpy as np
import scipy
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Medallion_Sales.csv', parse_dates=True, index_col='Date')

#data1 = pd.read_csv('Medallion_Sales.csv', parse_dates=True, index_col='Date')
#Change date from string to datetime
#data1['Date'] = pd.to_datetime(data1['Date'])
#ts = data1.set_index(['Date'])

#Rename column
data.rename(columns={'Sale Price':'Price'}, inplace=True)

data = data[::-1]
splitDate = '2011-05-01'

prior = data[:splitDate:]
post = data[splitDate::]

#plot new
plt.figure(1)
plt.plot(data.index,data,'*')
locs,labels = plt.yticks()
plt.yticks(locs, map(lambda x: "${:,}".format(x), locs))
plt.title("Medallion Prices over time")
plt.xlabel("Date")
plt.ylabel("Cost of Medallion")
plt.axvline(dt.datetime(2011,5,1))

#Histogram
plt.figure(2)
plt.hist(prior.as_matrix(), bins=50, color='r', label="Prior to Uber", alpha=.6)
plt.hist(post.as_matrix(), bins=50,color='b', label="Post Uber", alpha=.6)
locs,labels = plt.xticks()
plt.xticks(locs, map(lambda x: "${:,}".format(x), locs))
plt.title("Histogram of before/after Uber")
plt.xlabel("Cost of Medallion")
plt.ylabel("Number of Sales")
plt.legend()
#ts.columns


data.resample('1M',how='mean')
