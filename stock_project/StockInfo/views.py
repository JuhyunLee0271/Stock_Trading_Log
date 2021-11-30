from django.shortcuts import render, get_object_or_404
from django.db import connection
from .models import DayInfo, Stock
from .RealtimeInfo import TodayInfoCrawler
from datetime import datetime

sc = TodayInfoCrawler()
# 매 request 마다 update를 하는 것은 너무 비효율적인 것 같음
# 나중에 refresh 버튼 만들면 매핑해주면 좋을듯 
sc.UpdateStockPrice()

# 주식 종목 조회 
def list(request, page_num):
    stock_list = []
    
    # Stock 테이블이 비어있을 경우 [Stock_id, Name] 추가
    if Stock.objects.all().count() == 0:
        for code in sc.PRICE_NOW:
            Stock.objects.create(stock_id = code[0], name = code[1]['종목명'])
    
    # 1페이지 -> 거래대금 상위 1 ~ 10 , 2페이지 -> 거래대금 상위 11 ~ 20
    price_now = sc.PRICE_NOW[10*(page_num-1):10*(page_num)]

    # 주식 모든 종목들의 List: stock_list
    for code in price_now: 
        # print(code[1]['종목명'])
        stock_list.append([code[0], code[1]['종목명'], code[1]['등락률'], code[1]['종가'], code[1]['거래량'], int(code[1]['거래대금']//1000000)])
    
    context = {'stock_list': stock_list, 'time': datetime.now(), 'page_num': page_num}
    return render(request, 'StockInfo/stock_list.html', context)

def detail(request, stock_id, page_num):
    # sc.DAY_INFO
    # DB에 DAY_INFO 테이블에서 60일치 정보를 조회한다.
    stock_name = Stock.objects.get(stock_id = stock_id)
    stock_detail = DayInfo.objects.filter(stock = Stock.objects.get(stock_id = str(stock_id))).order_by('-date')
    
    context = {"stock_detail": stock_detail, "stock_name": stock_name, "page_num": page_num}

    return render(request, 'StockInfo/stock_detail.html', context)
