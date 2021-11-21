from django.shortcuts import render
from django.db import connection
from .models import Stock, Comment

# Create your views here.

# Controller 
def index(request):
    stockList = Stock.objects.all()
    context = {'stockList' : stockList}
    return render(request, 'StockInfo/stock_list.html', context)

def detail(request, stock_id):
    commentList = Comment.objects.filter(Stock_id = stock_id)
    context = {'commentList' : commentList}
    return render(request, 'StockInfo/stock_detail.html', context)
