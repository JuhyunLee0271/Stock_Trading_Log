from django.shortcuts import render
from django.db import connection
from .models import DayInfo, Stock, 
from .RealtimeInfo import TodayInfoCrawler

sc = TodayInfoCrawler()

# Controller
# 주식 종목 조회 
def list(request, page_num):
    # Update Stock Price
    sc.UpdateStockPrice()
    stock_list = []

    # 1페이지 -> 거래대금 상위 1 ~ 10 , 2페이지 -> 거래대금 상위 11 ~ 20
    price_now = sc.PRICE_NOW[10*(page_num-1):10*(page_num)]
   
    # [['삼성전자', 5.2, 74900, 27506623, 2047227974600], ['SK하이닉스', 7.17, 119500, 9786492, 1166463215825] ... ]
    for code in price_now:
        stock_list.append([code[1]['종목명'], code[1]['등락률'], code[1]['종가'], code[1]['거래량'], code[1]['거래대금']])
    
    context = {'stock_list': stock_list}
    return render(request, 'StockInfo/stock_list.html', context)

# 주식 상세 조회(60일치)
def detail(request, stock_id, page_num):
    
    # 60 DAY_INFO Query Set in LATEST ORDER
    stock_day_info = DayInfo.objects.filter(stock_id = stock_id).order_by('-date')[10*(page_num-1):10*(page_num)]
    stock = Stock.objects.get(stock_id = stock_id)

    context = {'stock_day_info' : stock_day_info, 'stock' : stock, 'page_num' : page_num}
    return render(request, 'StockInfo/stock_detail.html', context)
