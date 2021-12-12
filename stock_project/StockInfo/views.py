from time import time
from django.core import paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.db import connection
from .models import DayInfo, InterestedIn, Stock, User
from .RealtimeInfo import TodayInfoCrawler
from datetime import datetime
from django.core.paginator import Paginator

sc = TodayInfoCrawler()
sc.today = "20211207"
# 매 request 마다 update를 하는 것은 너무 비효율적인 것 같음
# 나중에 refresh 버튼 만들면 매핑해주면 좋을듯 
sc.UpdateStockPrice()

# 주식 종목 조회 
def list(request):
    stock_list = []
    
    # Stock 테이블이 비어있을 경우 [Stock_id, Name] 추가
    if Stock.objects.all().count() == 0:
        for code in sc.PRICE_NOW:
            Stock.objects.create(stock_id = code[0], name = code[1]['종목명'])
    
    # 1페이지 -> 거래대금 상위 1 ~ 10 , 2페이지 -> 거래대금 상위 11 ~ 20
    page = request.GET.get('page', '1')

    # 주식 모든 종목들의 List: stock_list
    for code in sc.PRICE_NOW: 
        # print(code[1]['종목명'])
        stock_list.append([code[0], code[1]['종목명'], code[1]['등락률'], code[1]['종가'], code[1]['거래량'], int(code[1]['거래대금']//1000000)])
    
    paginator = Paginator(stock_list, 10)
    page_obj = paginator.get_page(page)

    context = {'stock_list': page_obj, 'time': datetime.now()}
    return render(request, 'StockInfo/stock_list.html', context)

def detail(request, stock_id):
    # sc.DAY_INFO
    # DB에 DAY_INFO 테이블에서 60일치 정보를 조회한다.
    page = request.GET.get('page', '1')

    stock_name = Stock.objects.get(stock_id = stock_id)
    stock_detail = DayInfo.objects.filter(stock = Stock.objects.get(stock_id = str(stock_id))).order_by('-date')
    
    paginator = Paginator(stock_detail, 10)
    page_obj = paginator.get_page(page)
    if User.objects.all().count() == 0:
        User.objects.create(email = "aa.aa", nickname = "king", phone_number = "010-1234-5678")
    temp = User.objects.get(email = "aa.aa")
    ex =  InterestedIn.objects.filter(stock_id = stock_id, user = temp)
    
    context = {"stock_detail": page_obj, "stock_name": stock_name, "stock_interest": ex}

    return render(request, 'StockInfo/stock_detail.html', context)


def comment(request, stock_id):
    stock = get_object_or_404(Stock, pk = stock_id)
    if User.objects.all().count() == 0:
        User.objects.create(email = "aa.aa", nickname = "king", phone_number = "010-1234-5678")
    temp = User.objects.get(email = "aa.aa")
    stock.comment_set.create(content = request.POST.get('content'), create_time = datetime.now(), user = temp, stock = Stock.objects.get(stock_id = stock_id))
    return redirect('StockInfo:detail', stock_id = stock_id)

def interested(request, stock_id):
    stock = get_object_or_404(Stock, pk = stock_id)
    if User.objects.all().count() == 0:
        User.objects.create(email = "aa.aa", nickname = "king", phone_number = "010-1234-5678")
    temp = User.objects.get(email = "aa.aa")
    if InterestedIn.objects.filter(stock_id = stock_id, user = temp).exists():
        InterestedIn.objects.get(stock_id = stock_id, user = temp).delete()
    else:
        InterestedIn.objects.create(stock_id = stock.stock_id, user = temp)
    return redirect('StockInfo:detail', stock_id = stock_id)

def interestinfo(request):
    if User.objects.all().count() == 0:
        User.objects.create(email = "aa.aa", nickname = "king", phone_number = "010-1234-5678")
    temp = User.objects.get(email = "aa.aa")
    page = request.GET.get('page', '1')
    stock_list = []
    interlist = InterestedIn.objects.filter(user = temp)
    for inter in interlist:
        for code in sc.PRICE_NOW:
            if code[0] == inter.stock_id:
                stock_list.append([code[0], code[1]['종목명'], code[1]['등락률'], code[1]['종가'], code[1]['거래량'], int(code[1]['거래대금']//1000000)])
                break
    
    paginator = Paginator(stock_list, 10)
    page_obj = paginator.get_page(page)
    context = {"stock_list": page_obj, "time" : datetime.now()}
    return render(request, 'StockInfo/stock_list.html', context)