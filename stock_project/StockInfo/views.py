from django.shortcuts import render
from django.db import connection
from .models import DayInfo, Stock, Comment
from .RealtimeInfo import TodayInfoCrawler
from .DayInfo import DayInfoCrawler

# Create your views here.

# Controller 
def index(request):
    # Update Stock Price
    sc = TodayInfoCrawler();    sc.UpdateStockPrice()
    stockList = Stock.objects.all()
    context = {'stockList' : stockList}
    return render(request, 'StockInfo/stock_list.html', context)

def detail(request, stock_id):
    # sc.DAY_INFO
    return render(request, 'StockInfo/stock_detail.html', context)
