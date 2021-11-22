from django.urls import path
from . import views

app_name = 'StockInfo'

# StockInfo URL 매핑
urlpatterns = [
    # localhost:8080/StockInfo/<page_num>
    path('<int:page_num>', views.list, name='list'),
    path('detail/<int:stock_id>', views.detail, name='detail'),
]