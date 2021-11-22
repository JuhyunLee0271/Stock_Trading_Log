from pykrx import stock
import time
from datetime import datetime

from pykrx.website.krx import market

"""
ReatimeInfo.py
    KOSPI, KOSDAQ의 모든 종목들에 대해 매 10분마다 실시간(종가) 가격을 
    Price_now 딕셔너리에 저장
"""

# Class for "STOCK"
class TodayInfoCrawler:
    def __init__(self):
        self.CODE = stock.get_market_ticker_list(market="KOSPI") + stock.get_market_ticker_list(market="KOSDAQ")
        self.today = str(datetime.now().date()).replace('-','')
        self.KOSPI = None
        self.KOSDAQ = None
        self.PRICE_NOW = None
    
    def UpdateStockPrice(self):
        self.KOSPI = stock.get_market_ohlcv_by_ticker(self.today, market="KOSPI")['종가'].to_dict()
        time.sleep(1)
        self.KOSDAQ = stock.get_market_ohlcv_by_ticker(self.today, market="KOSDAQ")['종가'].to_dict()
        self.PRICE_NOW = dict(self.KOSPI, **self.KOSDAQ)

def main():
    sc = TodayInfoCrawler();    sc.UpdateStockPrice()
    print(len(sc.PRICE_NOW))
    
if __name__ == "__main__":
    main()