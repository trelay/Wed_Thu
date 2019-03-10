#!/usr/bin/env python3
#coding=utf-8
import matplotlib.pyplot as plt
import tushare as ts
from pandas import DataFrame
import pandas as pd
import numpy as np
import math

#df = ts.get_hist_data('000651')
df = ts.get_hist_data('sh')
df["Date"] = df.index

df['Date'] = pd.to_datetime(df['Date'])
df['Week_Number'] = df['Date'].dt.dayofweek


is_0 = df["Week_Number"] ==0
df_0 = df[is_0]

is_1 = df["Week_Number"] ==1
df_1 = df[is_1]

is_2 = df["Week_Number"] ==2
df_2 = df[is_2]

is_3 = df["Week_Number"] ==3
df_3 = df[is_3]

is_4 = df["Week_Number"] ==4
df_4 = df[is_4]

print("Let's compete the pprice(%) of dayofweek:")
print("Day_0: {}".format(df_0["p_change"].sum()))
print("Day_1: {}".format(df_1["p_change"].sum()))
print("Day_2: {}".format(df_2["p_change"].sum()))
print("Day_3: {}".format(df_3["p_change"].sum()))
print("Day_4: {}".format(df_4["p_change"].sum()))
"""
money = 50000
shares_own = 10

def sell_out(p_trade):
    global money
    global shares_own
    shares_act = shares_own
    shares_own = shares_own - shares_act
    money = money + shares_act * p_trade * 100

def buy_in(p_trade):
    global money
    global shares_own
    shares_act = math.floor(money/(p_trade*100))
    shares_own = shares_own + shares_act
    money = money - shares_act * p_trade * 100

data = df.sort_index(ascending=True)
for date in data.index:
    data_day_df = DataFrame(data, index=[date])
    Week_Number = DataFrame(data_day_df.T, index = ["Week_Number"]) .values[0][0]
    phigh = DataFrame(data_day_df.T, index = ["high"]) .values[0][0] 
    plow = DataFrame(data_day_df.T, index = ["low"]) .values[0][0]
    pclose = DataFrame(data_day_df.T, index = ["close"]) .values[0][0] 
    p_trade = (plow+ phigh)/2

    if int(Week_Number) == 1:
        sell_out(pclose)
    elif int(Week_Number) ==2:
        buy_in(pclose)

print('The money I have: {0}'.format(money))
print('The share I have: {0}'.format(shares_own))
"""
