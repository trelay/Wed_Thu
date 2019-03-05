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
rate_up = 0.7
rate_down = 0.5

p_yesterday_close= 0

price_last=()

def op_shares(price_last, popen_today):
    global money
    global shares_own
    price_move = abs(price_last[1]-price_last[3])

    shares_act = 0
    #if price_last[3] > (popen_today + price_move*rate_up):
    if price_last[3] < (popen_today - price_move*rate_down):
        print("Buying with price: {}".format(popen_today))
        shares_act = math.floor(money/(popen*100))
        shares_own = shares_own + shares_act

        money = money - shares_act * popen * 100
        print("I have totally share(*100):{}".format(shares_own))
        
    #elif price_last[3] < (popen_today - price_move*rate_down):
    elif price_last[3] > (popen_today + price_move*rate_up):
        print("Selling with price: {}".format(popen_today))
        shares_act = shares_own
        shares_own = shares_own - shares_act
        money = money + shares_act * popen * 100
        print("I have total money:{}".format(money))

data = df.sort_index(ascending=True)
t=0
for date in data.index:
    data_day_df = DataFrame(data, index=[date])
    popen = DataFrame(data_day_df.T, index = ["open"]) .values[0][0]
    pclose = DataFrame(data_day_df.T, index = ["close"]) .values[0][0] 
    phigh = DataFrame(data_day_df.T, index = ["high"]) .values[0][0] 
    plow = DataFrame(data_day_df.T, index = ["low"]) .values[0][0]
    if t>0:
        op_shares(price_last, popen)

    price_last = (popen,phigh,plow,pclose)

    t+=1

print('The money I have: {0}'.format(money))
print('The share I have: {0}'.format(shares_own))