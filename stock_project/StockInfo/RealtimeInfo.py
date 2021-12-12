from pykrx import stock
import time
from datetime import datetime

"""
ReatimeInfo.py
    KOSPI, KOSDAQ의 모든 종목들에 대해 매 10분마다 실시간(종가) 가격을 
    Price_now 딕셔너리에 저장
"""

# Class for "STOCK"
class TodayInfoCrawler:
    def __init__(self):
        self.CODE = stock.get_market_ticker_list(market="KOSPI") + stock.get_market_ticker_list(market="KOSDAQ")
        
        # 12시가 넘어가면 그날의 장 시작전까지는 정보가 없기 때문에
        # 테스트 시 today를 하드코딩 해야 됨 
        # self.today = str(datetime.now().date()).replace('-','')
        self.today = "20211125"
        self.KOSPI = None
        self.KOSDAQ = None
        self.PRICE_NOW = None
    
    def UpdateStockPrice(self):
        self.KOSPI = stock.get_market_price_change_by_ticker(self.today, self.today, market="KOSPI")[['종목명', '등락률', '종가', '거래량', '거래대금']].to_dict('index')
        time.sleep(1)
        self.KOSDAQ = stock.get_market_price_change_by_ticker(self.today, self.today, market="KOSDAQ")[['종목명', '등락률', '종가', '거래량', '거래대금']].to_dict('index')
        self.PRICE_NOW = sorted(dict(self.KOSPI, **self.KOSDAQ).items(), key=lambda x: -x[1]['거래대금'])

# def main():
#     sc = TodayInfoCrawler();    sc.UpdateStockPrice()
#     page_num = 1
#     price_now = sc.PRICE_NOW[10*(page_num-1):10*(page_num)]
#     stock_list = []
    
#     for code in price_now:
#         stock_list.append([code[1]['종목명'], code[1]['등락률'], code[1]['종가'], code[1]['거래량'], code[1]['거래대금']])
        
#     for stock in stock_list:
#         print(stock)

# if __name__ == "__main__":
#     main()