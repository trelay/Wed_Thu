#!/usr/bin/python3
#coding=utf-8
import requests
import re
import datetime
from time import sleep
from HTMLLogger import HTMLLogger
import pymysql
logger=HTMLLogger(name="Get daily tick", html_filename="tick.html", console_log=True)
 
def getHtml(url):
    sleep(2)
    try:
        r = requests.get(url)
    except:
        logger.error("Network error")
    if r.status_code ==200:
        r.encoding='gbk'
        return r.text
    else:
        logger.error("Resource is not reachable")
        return ""
 
def getTable(html):
    s = r'(?<=<table class="datatbl" id="datatbl">)([\s\S]*?)(?=</table>)'
    pat = re.compile(s)
    code = pat.findall(html)
    return code
 
def getTitle(tableString):
    s = r'(?<=<thead)>.*?([\s\S]*?)(?=</thead>)'
    pat = re.compile(s)
    code = pat.findall(tableString)
    s2 = r'(?<=<tr).*?>([\s\S]*?)(?=</tr>)'
    pat2 = re.compile(s2)
    code2 = pat2.findall(code[0])
    s3 = r'(?<=<t[h,d]).*?>([\s\S]*?)(?=</t[h,d]>)'
    pat3 = re.compile(s3)
    code3 = pat3.findall(code2[0])
    return code3

def format_chg(tick):
    # ['2018-06-01', '14:56:24', 10.19, 0, 112, 114128, True]

    tick[2] = float(tick[2])
    try:
        tick[3] = float(tick[3])
    except:
        tick[3] = 0
    tick[4] = int(tick[4])
    tick[5] = int(tick[5].replace(",",""))

    if tick[6]=='买盘':
        tick[6]=True
    else:
        tick[6]=False


def getBody(date, tableString):
    '''
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| date   | varchar(10) | NO   |     | NULL    |       |
| time   | varchar(8)  | NO   |     | NULL    |       |
| price  | float       | NO   |     | NULL    |       |
| p_chg  | float       | NO   |     | NULL    |       |
| share  | int(11)     | NO   |     | NULL    |       |
| volume | int(11)     | NO   |     | NULL    |       |
| action | tinyint(1)  | NO   |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
    '''
    s = r'(?<=<tbody)>.*?([\s\S]*?)(?=</tbody>)'
    pat = re.compile(s)
    code = pat.findall(tableString)
    s2 = r'(?<=<tr).*?>([\s\S]*?)(?=</tr>)'
    pat2 = re.compile(s2)
    code2 = pat2.findall(code[0])
    s3 = r'(?<=<t[h,d]).*?>(?!<)([\s\S]*?)(?=</)[^>]*>'
    pat3 = re.compile(s3)
    code3 = []
    for tr in code2:
        tick = pat3.findall(tr)
        tick.insert(0, date)
        try:
            format_chg(tick)
        except:
            logger.error("Failed to change the format of tick: {}".format(str(tick)))
        code3.append(str(tuple(tick)))
    return code3

def get_tick(dateObj,symbol):

    date = dateObj.strftime("%Y-%m-%d")
    daily_tick = []
    page = 1
    while True:
        url = 'http://market.finance.sina.com.cn/transHis.php?symbol=' + symbol + '&date=' + date + '&page=' + str(page)
        html = getHtml(url)
        table = getTable(html)
        if len(table) != 0:
            tbody = getBody(date,table[0])
            daily_tick = daily_tick + tbody
            if len(tbody) == 0:
                logger.info("Finished getting daily tick for {} on {}".format(symbol,date))
                break
            if page == 1:
                thead = getTitle(table[0])
        else:
            logger.warning("No data on {}".format(date))
            break
        page += 1
        #break;

    daily_tick.reverse()
    return daily_tick

def insert_data(mysql_cmd):
    db = pymysql.connect("192.168.0.106","tick_user","426942","Ticks" )
    cursor = db.cursor()

    try:
        cursor.execute(mysql_cmd)
        db.commit()
    except:
        db.rollback()
    db.close()

def main(symbol):
    
    date_Obj = datetime.datetime(2010, 4, 4)
    while datetime.datetime.now() > date_Obj:
        
        if date_Obj.weekday() <6:
            daily_tick = get_tick(date_Obj,symbol)
            values = ","
            values = values.join(daily_tick)
            if len(values) >0:

                mysql_cmd = "insert into sz000001 (date, time, price, p_chg, share, volume, action) values " + values
                insert_data(mysql_cmd)
        date_Obj = date_Obj+ datetime.timedelta(days=1)

if __name__ == "__main__":
    symbol = 'sz000001'
    main(symbol)