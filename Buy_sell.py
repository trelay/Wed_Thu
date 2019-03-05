#!/usr/bin/env python3
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

money = 50000
shares_own = 10
shares_total = shares_own

action = 0
rate = 0
p_Base= 0
rate_up = 0.7
rate_down = 0.5

p_yesterday_close= 0



def op_shares(action,rate,p_yesterday_close, popen):
    global money
    global shares_own
    global shares_total

    shares_act = 0
    if action == 1 and popen > (p_yesterday_close*(1+ rate* rate_up)):
        print("Buying")
        shares_act = math.floor(money/(popen*100))
        shares_total = shares_own + shares_act
        money = money - shares_act * popen * 100
        
    elif action == -1 and popen < (p_yesterday_close*(1- rate* rate_down)):
        print("sell")
        shares_act = math.floor(money/(popen*100))
        shares_total = shares_own - shares_act
        money = money + shares_act * popen * 100

data = df.sort_index(ascending=True)
t=0
for date in data.index:
    #print(date)
    data_day_df = DataFrame(data, index=[date])
    popen = DataFrame(data_day_df.T, index = ["open"]) .values[0][0]
    pclose = DataFrame(data_day_df.T, index = ["close"]) .values[0][0] 
    phigh = DataFrame(data_day_df.T, index = ["high"]) .values[0][0] 
    plow = DataFrame(data_day_df.T, index = ["low"]) .values[0][0]

    if t>0:
        op_shares(action,rate,p_yesterday_close,popen)

    if phigh == pclose:
        action = 0
        rate = 0
    elif phigh > pclose:
        action = 1
        rate = (phigh - pclose)/pclose
    elif phigh < pclose:
        action == -1
        rate = (pclose - phigh)/pclose

    p_yesterday_close = pclose

    t+=1

print('The money I have: {0}'.format(money))
print('The share I have: {0}'.format(shares_total))