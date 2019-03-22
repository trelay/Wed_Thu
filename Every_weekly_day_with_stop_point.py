#!/usr/bin/env python3
#coding=utf-8
import matplotlib.pyplot as plt
import tushare as ts
from pandas import DataFrame
import pandas as pd
import numpy as np
import math

money = 50000
shares_own = 10
buy_price = 0

def get_hist_df(code):
    df = ts.get_hist_data(code)
    #df = ts.get_hist_data('sh')
    #df = ts.get_hist_data('sz')
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

    #print("Let's compete the pprice(%) of dayofweek:")
    #print("Day_0: {}, Days_of_>0: {}, Days_of_<0: {}".format(df_0["p_change"].sum(), (df_0['p_change']>0).sum(), (df_0['p_change']<0).sum()))
    #print("Day_1: {}, Days_of_>0: {}, Days_of_<0: {}".format(df_1["p_change"].sum(), (df_1['p_change']>0).sum(), (df_1['p_change']<0).sum()))
    #print("Day_2: {}, Days_of_>0: {}, Days_of_<0: {}".format(df_2["p_change"].sum(), (df_2['p_change']>0).sum(), (df_2['p_change']<0).sum()))
    #print("Day_3: {}, Days_of_>0: {}, Days_of_<0: {}".format(df_3["p_change"].sum(), (df_3['p_change']>0).sum(), (df_3['p_change']<0).sum()))
    #print("Day_4: {}, Days_of_>0: {}, Days_of_<0: {}".format(df_4["p_change"].sum(), (df_4['p_change']>0).sum(), (df_4['p_change']<0).sum()))
    return df

def trade_share(df, lose_point):

    global buy_price
    service_1 = 2/10000
    service_2 = 1/1000
    share_on_hand = True
    buy_in_act = 0.0

    def sell_out(p_trade):
        global money
        global shares_own
        #########################################
        shares_act = shares_own
        shares_own = shares_own - shares_act
        money_trade = shares_act * p_trade * 100
        #########################################
        money = money +  money_trade -(money_trade *(service_1 + service_2))

    def buy_in(p_trade):
        global money
        global shares_own
        #########################################
        shares_act = math.floor(money/(p_trade*100))
        shares_own = shares_own + shares_act
        money_trade = shares_act * p_trade * 100
        #########################################
        money = money - money_trade - (money_trade *service_1)

    data = df.sort_index(ascending=True)
    for date in data.index:
        data_day_df = DataFrame(data, index=[date])
        Week_Number = DataFrame(data_day_df.T, index = ["Week_Number"]) .values[0][0]

        popen = DataFrame(data_day_df.T, index = ["open"]) .values[0][0] 
        phigh = DataFrame(data_day_df.T, index = ["high"]) .values[0][0] 
        plow = DataFrame(data_day_df.T, index = ["low"]) .values[0][0]
        pclose = DataFrame(data_day_df.T, index = ["close"]) .values[0][0] 
        p_trade_s = ((plow+ phigh)/2 + phigh)/2
        p_trade_b = ((plow+ phigh)/2 + plow)/2

        if int(Week_Number) == 1 and p_trade_s > buy_price:
            sell_out(p_trade_s)
            share_on_hand = False
        elif int(Week_Number) ==3:
            buy_in_act = p_trade_b
            buy_price = p_trade_b
            buy_in(p_trade_b)
            share_on_hand = True
        
        if share_on_hand and popen< buy_in_act*(1-lose_point):
            sell_out(popen)

    #print('The money I have: {0}'.format(money))
    #print('The share I have: {0}'.format(shares_own))
    gross_margin = int((money + shares_own*100*pclose)/10000)
    print("Money I have: {0}".format(gross_margin))


if __name__=="__main__":
    '''
    lose_point =0.01
    while lose_point <0.10:

        money = 50000
        shares_own = 10
        df = get_hist_df("000651")
        print("Trade_stop_point: {0}".format(lose_point*100))
        trade_share(df, lose_point)
        lose_point +=0.01
    '''
    lose_point =0.05
    df = get_hist_df("000651")
    print("Trade_stop_point: {0}".format(lose_point*100))
    trade_share(df, lose_point)
