# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# USER, STOCK, DAY_INFO, COMMENT, COMMENT_LIKE, INTERESTED_IN, TRADE_RECORD

class Comment(models.Model):
    post_id = models.AutoField(db_column='Post_id', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=30)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='Create_time')  # Field name made lowercase.
    user = models.OneToOneField('User', on_delete=models.CASCADE, db_column='User_id')  # Field name made lowercase.
    stock = models.OneToOneField('Stock', on_delete=models.CASCADE, db_column='Stock_id')  # Field name made lowercase.

    class Meta:
        db_table = 'comment'

class CommentLike(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, db_column='User_id', primary_key=True)  # Field name made lowercase.
    post = models.OneToOneField(Comment, on_delete=models.CASCADE, db_column='Post_id')  # Field name made lowercase.
    like = models.CharField(db_column='Like', max_length=1)  # Field name made lowercase.

    class Meta:
        db_table = 'comment_like'
        unique_together = (('user', 'post'),)

class DayInfo(models.Model):
    stock = models.OneToOneField('Stock', on_delete=models.CASCADE, db_column='Stock_id', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    shares = models.IntegerField(db_column='Shares')  # Field name made lowercase.
    per = models.FloatField(db_column='Per')  # Field name made lowercase.
    volume = models.IntegerField(db_column='Volume')  # Field name made lowercase.
    market_cap = models.IntegerField(db_column='Market_cap')  # Field name made lowercase.
    roe = models.FloatField(db_column='Roe')  # Field name made lowercase.
    transaction_amount = models.IntegerField(db_column='Transaction_amount')  # Field name made lowercase.
    foreigner_rate = models.FloatField(db_column='Foreigner_rate')  # Field name made lowercase.
    par_value = models.IntegerField(db_column='Par_value')  # Field name made lowercase.

    class Meta:
        db_table = 'day_info'
        unique_together = (('stock', 'date'),)

class InterestedIn(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, db_column='User_id', primary_key=True)  # Field name made lowercase.
    stock = models.OneToOneField('Stock', on_delete=models.CASCADE, db_column='Stock_id')  # Field name made lowercase.

    class Meta:
        db_table = 'interested_in'
        unique_together = (('user', 'stock'),)

class Stock(models.Model):
    stock_id = models.IntegerField(db_column='Stock_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=30)  # Field name made lowercase.
    last_update = models.DateTimeField(db_column='Last_update')  # Field name made lowercase.

    class Meta:
        db_table = 'stock'

class TradeRecord(models.Model):
    record_id = models.AutoField(db_column='Record_id', primary_key=True)  # Field name made lowercase.
    trade_price = models.IntegerField(db_column='Trade_price')  # Field name made lowercase.
    trade_quantity = models.IntegerField(db_column='Trade_quantity')  # Field name made lowercase.
    trade_type = models.CharField(db_column='Trade_type', max_length=1)  # Field name made lowercase.
    trade_date = models.DateTimeField(db_column='Trade_date')  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    user = models.OneToOneField('User', on_delete=models.CASCADE, db_column='User_id')  # Field name made lowercase.
    stock = models.OneToOneField(Stock, on_delete=models.CASCADE, db_column='Stock_id')  # Field name made lowercase.

    class Meta:
        db_table = 'trade_record'

class User(models.Model):
    user_id = models.AutoField(db_column='User_id', primary_key=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=30)  # Field name made lowercase.
    nickname = models.CharField(db_column='Nickname', unique=True, max_length=30)  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone_number', unique=True, max_length=30)  # Field name made lowercase.

    class Meta:
        db_table = 'user'
