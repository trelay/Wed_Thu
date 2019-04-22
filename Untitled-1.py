#!/usr/bin/python
import datetime
import pymysql.cursors
conn = pymysql.connect(host='127.0.0.1',
               port=3306,
               user='root',
               password='',
               db='test',
               charset='utf8',
               cursorclass=pymysql.cursors.DictCursor)
#中间略去dt赋值部分...
print(dt.strftime('%Y-%m-%d %H:%M:%S'))
#运行结果是 2001-1-2 11：00：00
sql_insert=sql_insert="INSERT into tablename(exTime) values(%s)" %(dt.strftime("%Y-%m-%d %H:%M:%S"))
#如果此处写成sql_insert=sql_insert="INSERT into tablename(exTime) values('2001-1-2 11：00：00')" 则可以运行
 
try:
  with conn.cursor() as csor1:
     
    csor1.execute(sql_insert)
    conn.commit()
    csor1.close()
except Exception as e:
  #错误回滚
  conn.rollback()
finally:
  conn.close()