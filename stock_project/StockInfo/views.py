from django.shortcuts import render
from django.db import connection
from .models import DayInfo, Stock, Comment
from .RealtimeInfo import TodayInfoCrawler
from .DayInfo import DayInfoCrawler

# Controller 
def list(request, page_num):
    # Update Stock Price
    sc = TodayInfoCrawler();    sc.UpdateStockPrice()
        
    # 1페이지 -> 거래대금 상위 1 ~ 10 , 2페이지 -> 거래대금 상위 11 ~ 20
    price_now = sc.PRICE_NOW[10*(page_num-1):10*(page_num)]
    stock_list = []

    for code in price_now:
        # [['삼성전자', 5.2, 74900, 27506623, 2047227974600], ['SK하이닉스', 7.17, 119500, 9786492, 1166463215825] ... ]
        stock_list.append([code[1]['종목명'], code[1]['등락률'], code[1]['종가'], code[1]['거래량'], code[1]['거래대금']])
    
    context = {'stock_list': stock_list}
    return render(request, 'StockInfo/stock_list.html', context)

def detail(request, stock_id):
    # sc.DAY_INFO
    pass
    # return render(request, 'StockInfo/stock_detail.html', context)
