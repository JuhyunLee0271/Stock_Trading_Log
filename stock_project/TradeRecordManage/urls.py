from django.urls import path
from . import views

app_name = 'TradeRecordManage'

# TradeRecordManage
urlpatterns = [
    path('', views.index, name='index'),
]