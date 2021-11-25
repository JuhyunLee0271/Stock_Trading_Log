from pykrx import stock
import pandas as pd
import time
from datetime import datetime, timedelta

# Class for "DAY_INFO"
class DayInfoCrawler:
    
    def __init__(self, interval):
        self.CODE = stock.get_market_ticker_list(market="KOSPI") + stock.get_market_ticker_list(market="KOSDAQ")
        self.interval = interval
        self.today = datetime.now().date()
        self.days = []
        self.DAY_INFO = dict()

    def GetWeekDays(self):
        startDate = self.today
        while len(self.days) < self.interval:
            if 0 <= startDate.weekday() <= 4:
                # weekday = str(startDate).replace('-','')
                self.days.append(startDate)
            startDate -= timedelta(1)
        self.days.reverse()

    def GetDayInfo(self):
        for day in self.days:
            date = str(day).replace('-', '')
            ohlcv_1 = stock.get_market_ohlcv_by_ticker(date, market="KOSPI"); time.sleep(1)
            ohlcv_2 = stock.get_market_ohlcv_by_ticker(date, market="KOSDAQ"); time.sleep(1)
            fundamental_1 = stock.get_market_fundamental_by_ticker(date, market="KOSPI"); time.sleep(1)
            fundamental_2 = stock.get_market_fundamental_by_ticker(date, market="KOSDAQ"); time.sleep(1)
            marketcap_1 = stock.get_market_cap_by_ticker(date, market="KOSPI"); time.sleep(1)
            marketcap_2 = stock.get_market_cap_by_ticker(date, market="KOSDAQ"); time.sleep(1)

            ohlcv = pd.concat([ohlcv_1, ohlcv_2],axis=0, join='inner')
            fundamental = pd.concat([fundamental_1, fundamental_2],axis=0, join='inner')
            marketcap = pd.concat([marketcap_1, marketcap_2],axis=0, join='inner')

            one_day_info = pd.concat([ohlcv, fundamental, marketcap], axis=1, join='inner').to_dict('index')
            self.DAY_INFO[day] = one_day_info
