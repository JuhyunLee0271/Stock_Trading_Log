from django.contrib import admin
from .models import User, Stock, Comment, CommentLike, InterestedIn, DayInfo, TradeRecord
# Register your models here.

# Managed by admin user
admin.site.register(User)
admin.site.register(Stock)
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(InterestedIn)
admin.site.register(DayInfo)
admin.site.register(TradeRecord)