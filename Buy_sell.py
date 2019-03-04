#!/usr/bin/env python2
#coding=utf-8
import matplotlib.pyplot as plt
import tushare as ts
from pandas import DataFrame
import pandas as pd
import numpy as np
import math


df = ts.get_hist_data('000651')

#fig = plt.figure()
#gree_test = DataFrame(df, columns = ["open", "close", "high"])
#data_2019=gree_test["close"].sort_index(ascending=True)
#data_2019.cumsum()
#data_2019.plot()
#plt.show()

shares_own = 1000
shares_inv = 1000
shares_act = 0

action = 0
rate = 0

def op_shares(action,rate,date):
    if action == 1:
        shares_act = 
        shares_inv = 0

        
    elif action ==-1:
        shares_inv = shares_inv + shares_own
        shares_own = 0

data = df.sort_index(ascending=True)
t=0
for date in data.index:
    
    data_day_df = DataFrame(data, index=[i])
    popen = DataFrame(data_day_df.T, index = ["open"]) .values[0][0]
    pclose = DataFrame(data_day_df.T, index = ["close"]) .values[0][0] 
    phigh = DataFrame(data_day_df.T, index = ["high"]) .values[0][0] 
    plow = DataFrame(data_day_df.T, index = ["low"]) .values[0][0]

    if t>0:
        op_shares(action,rate,date)
    else:
        money = shares_own * pclose

    if phigh = pclose:
        action = 0
        rate = 0
    elif phigh > pclose:
        action = 1
        rate = (phigh - pclose)/pclose
    else:
        action = -1
        rate = (pclose - phigh)/pclose

    t+=1