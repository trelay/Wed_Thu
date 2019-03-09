#!/usr/bin/env python3
#coding=utf-8
import matplotlib.pyplot as plt
import tushare as ts
from pandas import DataFrame
import pandas as pd
import numpy as np
import math


df = ts.get_hist_data('000651')
df["Date"] = df.index

df['Date'] = pd.to_datetime(df['Date'])
df['Week_Number'] = df['Date'].dt.dayofweek
del df["Date"]

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

print("Let's compete:")
print("Day_1: {}".format(df_0["p_change"].sum()))
print("Day_2: {}".format(df_1["p_change"].sum()))
print("Day_3: {}".format(df_2["p_change"].sum()))
print("Day_4: {}".format(df_3["p_change"].sum()))
print("Day_5: {}".format(df_4["p_change"].sum()))