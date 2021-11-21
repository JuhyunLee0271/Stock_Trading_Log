from django.contrib import admin
from StockInfo.models import User, Stock, Comment, Interested_in
# Register your models here.

admin.site.register(User)
admin.site.register(Stock)
admin.site.register(Comment)
admin.site.register(Interested_in)
