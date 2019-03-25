import tushare as ts
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