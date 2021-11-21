from django.urls import path
from . import views

app_name = 'StockInfo'

# StockInfo URL 매핑
urlpatterns = [
    # localhost:8080/StockInfo/ -> index 메서드 처리
    path('', views.index, name='index'),
    path('<int:stock_id>', views.detail, name='detail'),
]