from django.shortcuts import render, get_object_or_404
from django.db import connection
from .models import DayInfo, Stock, 
from .RealtimeInfo import TodayInfoCrawler
from .DayInfo import DayInfoCrawler

sc = TodayInfoCrawler()

# Controller
# 주식 종목 조회 
def list(request, page_num):
    # Update Stock Price
    sc.UpdateStockPrice()
    stock_list = []
    if Stock.objects.all().count() == 0:
        for code in sc.PRICE_NOW:
            Stock.objects.create(stock_id = code[0], name = code[1]['종목명'])
    # 1페이지 -> 거래대금 상위 1 ~ 10 , 2페이지 -> 거래대금 상위 11 ~ 20
    price_now = sc.PRICE_NOW[10*(page_num-1):10*(page_num)]
    for code in price_now: 
        print(code[1]['종목명'])
        stock_list.append([code[1]['종목명'], code[1]['등락률'], code[1]['종가'], code[1]['거래량'], code[1]['거래대금']])
    # stock_list = Stock.objects.filter(last_update = time)
    context = {'stock_list': stock_list, 'time': time}
    return render(request, 'StockInfo/stock_list.html', context)

def detail(request, stock_id):
    # sc.DAY_INFO
    sc = DayInfoCrawler(4)
    sc.GetWeekDays()
    sc.GetDayInfo()
    
    for day, datas in sc.DAY_INFO.items():
        if DayInfo.objects.filter(date = day).count() > 0:
            continue
        for id, data in datas.items():
            temp = get_object_or_404(Stock, stock_id = stock_id)
            DayInfo.objects.create(stock = Stock.objects.get(stock_id = id), date = day, open_price = data['시가'],
            high_price = data['고가'], low_price = data['저가'], close_price = data['종가'], 
            transaction_amount = data['거래대금'] // 1000000, rate = data['등락률'],
            BPS = data['BPS'], PER = data['PER'], PBR = data['PBR'], EPS = data['EPS'],
            market_cap = data['시가총액'] // 100000000)

    context = {"stock_detail" : DayInfo.objects.filter(stock = Stock.objects.get(stock_id = str(stock_id))).order_by('date')}
    
    return render(request, 'StockInfo/stock_detail.html', context)
