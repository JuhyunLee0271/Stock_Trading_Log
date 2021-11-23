from django.shortcuts import render
from django.db import connection
from .models import DayInfo, Stock, Comment
from .RealtimeInfo import TodayInfoCrawler
from .DayInfo import DayInfoCrawler
from django.utils import timezone

# Controller 
def list(request, page_num):
    # Update Stock Price
    sc = TodayInfoCrawler()
    sc.UpdateStockPrice()
    time = timezone.now()
    stock_list = []
    # 1페이지 -> 거래대금 상위 1 ~ 10 , 2페이지 -> 거래대금 상위 11 ~ 20
    price_now = sc.PRICE_NOW[10*(page_num-1):10*(page_num)]
    for code in price_now:
        count = Stock.objects.filter(stock_id = int(code[0])).count()
        if count > 0:
            temp = Stock.objects.get(stock_id = int(code[0]))
            temp.last_update = time
            temp.save()
        # [['삼성전자', 5.2, 74900, 27506623, 2047227974600], ['SK하이닉스', 7.17, 119500, 9786492, 1166463215825] ... ]
        else:    
            temp = Stock.objects.create(stock_id = int(code[0]), name = code[1]['종목명'], last_update = time)
        stock_list.append([code[1]['종목명'], code[1]['등락률'], code[1]['종가'], code[1]['거래량'], code[1]['거래대금']])
    # stock_list = Stock.objects.filter(last_update = time)
    context = {'stock_list': stock_list}
    print(context)
    return render(request, 'StockInfo/stock_list.html', context)

def detail(request, stock_id):
    # sc.DAY_INFO
    pass
    # return render(request, 'StockInfo/stock_detail.html', context)
