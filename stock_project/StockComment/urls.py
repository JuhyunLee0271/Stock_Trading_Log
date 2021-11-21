from django.urls import path
from . import views

app_name = 'StockComment'

# StockComment
urlpatterns = [
    path('', views.index, name='index'),
]