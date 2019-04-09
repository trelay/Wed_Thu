#!/usr/bin/python3
#coding=utf-8
import matplotlib.pyplot as plt
import tushare as ts
from pandas import DataFrame
import pandas as pd
import numpy as np
import math
token = '418443b56e07ac5c235d232406b44db8f80484569f8240f4554c6d67'

money = 50000
shares_own = 10

def get_hist_df(code):
    pro = ts.pro_api(token)
    df = pro.query('daily', ts_code=code, start_date='20160701', end_date='20190322')
    #df = pro.query('daily', ts_code=code, start_date='20190302', end_date='20190322')

    df['trade_date'] = pd.to_datetime(df['trade_date'])
    df['Week_Number'] = df['trade_date'].dt.dayofweek
    df.index = df['trade_date']
    del df['trade_date']

    return df

class init_list(object):
    def __init__(self,size):
        self.list = [0]*size
        self.size = size
    def get(self):
        return self.list
    def add(self, ele):
        self.list.append(ele)
        self.list = self.list[-self.size:]

def trade_share(df):

    service_1 = 1.6/10000
    service_2 = 1/1000

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

    data = df.sort_values(by='trade_date',ascending = True)

    for trade_date in data.index:
        data_day_df = DataFrame(data, index=[trade_date])
        Week_Number = DataFrame(data_day_df.T, index = ["Week_Number"]) .values[0][0]

        popen = DataFrame(data_day_df.T, index = ["open"]) .values[0][0] 
        phigh = DataFrame(data_day_df.T, index = ["high"]) .values[0][0] 
        plow = DataFrame(data_day_df.T, index = ["low"]) .values[0][0]
        ppchange = DataFrame(data_day_df.T, index = ["pct_chg"]) .values[0][0]
        pclose = DataFrame(data_day_df.T, index = ["close"]) .values[0][0] 
        #p_trade_s = ((plow+ phigh)/2 + phigh)/2
        #p_trade_b = ((plow+ phigh)/2 + plow)/2
        if sum(up_list.get()) == up_signal:
            sell_out(popen)

        elif sum(down_list.get()) == down_signal:
            buy_in(popen)

        if ppchange > 1.0:
            up_list.add(1)
            down_list.add(0)
        elif ppchange < -1.0:
            up_list.add(0)
            down_list.add(1)
        else:
            up_list.add(0)
            down_list.add(0)


        tmp_margin = int((money + shares_own*100*pclose)/10000)
        print("On {} tmp_margin I have: {}".format(trade_date, tmp_margin))

    gross_margin = int((money + shares_own*100*pclose)/10000)
    print("Money I have: {0}".format(gross_margin))



if __name__ == "__main__":
    up_signal = 2
    down_signal = 2

    up_list = init_list(up_signal)
    down_list = init_list(down_signal)
    df = get_hist_df("000651.sz")
    print(df)
    trade_share(df)

