#!/usr/bin/env python3
#coding=utf-8
import matplotlib.pyplot as plt
import tushare as ts
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import math

share_code = "sz"

#df = ts.get_hist_data(share_code)
#df = ts.get_hist_data('sh')
df = ts.get_hist_data('sz')
df["Date"] = df.index

df['Date'] = pd.to_datetime(df['Date'])
#df = df[df["Date"]> pd.to_datetime("2018-01-23")]

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


highest = Series([])
for trade_date in df_2.index:
    
    #df_x = ts.get_tick_data(share_code,date=trade_date,src='tt')
    try:
        df_x = ts.get_tick_data(share_code,date=trade_date,src='tt')
        trade_time = df_x[df_x["price"] == df_x["price"].min()]["time"].iloc[0]
    except:
        trade_time = ""
        pass
    if trade_time != "":
        tmp_time = trade_time.split(":")
        highest[trade_date] = int(tmp_time[0])+int(tmp_time[0])/60

after = highest[highest > 12]
morning = highest[highest < 12]

print("Totall found {} lowest on Wed.".format(highest.count()))
print("Highest price happen {} times before 10:30 on the morning.".format(morning[morning<10.5].count()))
print("Highest price happen {} times after 10:30 on the morning.".format(morning[morning>10.5].count()))
print("Highest price happen {} times before 14:00 on the afternoon".format(after[after<14].count()))
print("Highest price happen {} times after 14:00 on the afternoon".format(after[after>14].count()))




highest = Series([])
for trade_date in df_1.index:
    
    #df_x = ts.get_tick_data(share_code,date=trade_date,src='tt')
    try:
        df_x = ts.get_tick_data(share_code,date=trade_date,src='tt')
        trade_time = df_x[df_x["price"] == df_x["price"].max()]["time"].iloc[0]
    except:
        trade_time = ""
        pass
    if trade_time != "":
        tmp_time = trade_time.split(":")
        highest[trade_date] = int(tmp_time[0])+int(tmp_time[0])/60

after = highest[highest > 12]
morning = highest[highest < 12]

print("Totall found {} highest on Tus.".format(highest.count()))
print("Highest price happen {} times before 10:30 on the morning.".format(morning[morning<10.5].count()))
print("Highest price happen {} times after 10:30 on the morning.".format(morning[morning>10.5].count()))
print("Highest price happen {} times before 14:00 on the afternoon".format(after[after<14].count()))
print("Highest price happen {} times after 14:00 on the afternoon".format(after[after>14].count()))