#!/usr/bin/env python3
#coding=utf-8
import matplotlib.pyplot as plt
import tushare as ts
from pandas import DataFrame
import pandas as pd
import numpy as np
import math

money = 300000
shares_own = 10
buy_price = 0

def get_hist_df(code):
    pro = ts.pro_api('418443b56e07ac5c235d232406b44db8f80484569f8240f4554c6d67')
    df = pro.query('daily', ts_code='000651.SZ', start_date='20160701', end_date='20190322')

    df['trade_date'] = pd.to_datetime(df['trade_date'])
    df['Week_Number'] = df['trade_date'].dt.dayofweek

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
    print("Day_0: {}, Days_of_>0: {}, Days_of_<0: {}".format(df_0["pct_chg"].sum(), (df_0['pct_chg']>0).sum(), (df_0['pct_chg']<0).sum()))
    print("Day_1: {}, Days_of_>0: {}, Days_of_<0: {}".format(df_1["pct_chg"].sum(), (df_1['pct_chg']>0).sum(), (df_1['pct_chg']<0).sum()))
    print("Day_2: {}, Days_of_>0: {}, Days_of_<0: {}".format(df_2["pct_chg"].sum(), (df_2['pct_chg']>0).sum(), (df_2['pct_chg']<0).sum()))
    print("Day_3: {}, Days_of_>0: {}, Days_of_<0: {}".format(df_3["pct_chg"].sum(), (df_3['pct_chg']>0).sum(), (df_3['pct_chg']<0).sum()))
    print("Day_4: {}, Days_of_>0: {}, Days_of_<0: {}".format(df_4["pct_chg"].sum(), (df_4['pct_chg']>0).sum(), (df_4['pct_chg']<0).sum()))
    
    return df_2

if __name__=="__main__":
    df_2 = get_hist_df("000651")
    print(df_2)