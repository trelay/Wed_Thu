#!/usr/bin/env python2
#coding=utf-8
import matplotlib.pyplot as plt
import tushare as ts
from pandas import DataFrame
import pandas as pd
import numpy as np

df = ts.get_hist_data('000651')
gree_test = DataFrame(df, columns = ["open", "close", "high"])

fig = plt.figure()

data_2019=gree_test["close"].sort_index(ascending=True)
data_2019.cumsum()
data_2019.plot()
plt.show()
