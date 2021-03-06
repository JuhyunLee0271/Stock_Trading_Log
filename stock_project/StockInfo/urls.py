from django.urls import path
from . import views

app_name = 'StockInfo'

# StockInfo URL 매핑
urlpatterns = [

    # localhost:8080/StockInfo/<page_num>
    # 거래대금이 높은 순으로 실시간 주식 정보 조회
    path('', views.list, name='list'),

    # localhost:8080/StockInfo/detail/<stock_id>/<page_num>
    # 각 주식별 60일치 정보인 DAY_INFO를 조회
    path('detail/<str:stock_id>/', views.detail, name='detail'),
    path('detail/<str:stock_id>/comment', views.comment, name='comment'),
    path('interest/<str:stock_id>/', views.interested, name="interested"),
    path('interestinfo/', views.interestinfo, name="interestinfo")
]