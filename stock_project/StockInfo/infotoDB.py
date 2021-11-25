from DayInfo import DayInfoCrawler
from datetime import datetime
from django.db import connection
# from models import DayInfo, Stock


sc = DayInfoCrawler(2)
sc.GetWeekDays()
sc.GetDayInfo()

for day, datas in sc.DAY_INFO.items():
    for id, data in datas.items():
        info = data.items()
        print(info)
        # DayInfo.objects.create(stock = Stock.objects.get(stock_id = int(id)), date = day, open_price = info['시가'],
        # high_price = info['고가'], low_price = info['저가'], close_price = info['종가'], 
        # volume = info['거래량'], transaction_amount = info['거래대금'], rate = info['등락률'],
        # BPS = info['BPS'], PER = info['PER'], PBR = info['PBR'], EPS = info['EPS'],
        # DIV = info['DIV'], DPS = info['DPS'], market_cap = info['시가총액'], shares = info['상장주식수'])