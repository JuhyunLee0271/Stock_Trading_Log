# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django import db
from django.db import models

# USER, STOCK, DAY_INFO, COMMENT, COMMENT_LIKE, INTERESTED_IN, TRADE_RECORD
class Stock(models.Model):
    stock_id = models.CharField(db_column='Stock_id', primary_key=True, max_length=6)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=30)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'stock'

class Comment(models.Model):
    post_id = models.AutoField(db_column='Post_id', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=30)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='Create_time')  # Field name made lowercase.
    user = models.ForeignKey('User', on_delete = models.CASCADE, db_column='User_id')  # Field name made lowercase.
    stock = models.ForeignKey('Stock', on_delete = models.CASCADE, db_column='Stock_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'comment'

class CommentLike(models.Model):
    user = models.OneToOneField('User', on_delete = models.CASCADE, db_column='User_id', primary_key=True)  # Field name made lowercase.
    post = models.ForeignKey(Comment, on_delete = models.CASCADE, db_column='Post_id')  # Field name made lowercase.
    like = models.CharField(db_column='Like', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'comment_like'
        unique_together = (('user', 'post'),)

class DayInfo(models.Model):
    info_id = models.AutoField(primary_key=True)
    stock = models.ForeignKey('Stock', on_delete = models.CASCADE, db_column='Stock_id')
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    open_price = models.IntegerField(db_column='open_price')
    high_price = models.IntegerField(db_column='high_price')
    low_price = models.IntegerField(db_column='low_price')
    closing_price = models.IntegerField(db_column='closing_price')
    transaction_value = models.IntegerField(db_column='transaction_value')
    transaction_amount = models.IntegerField(db_column='transaction_amount')
    fluctuation_rate = models.FloatField(db_column='fluctuation_rate')
    bps = models.FloatField(db_column='BPS')  # Field name made lowercase.
    per = models.FloatField(db_column='PER')  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR')  # Field name made lowercase.
    eps = models.FloatField(db_column='EPS')  # Field name made lowercase.
    market_cap = models.IntegerField(db_column='market_cap')

    class Meta:
        managed = True
        db_table = 'day_info'

class InterestedIn(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, db_column='User_id', primary_key=True)  # Field name made lowercase.
    stock = models.ForeignKey('Stock', models.DO_NOTHING, db_column='Stock_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'interested_in'
        unique_together = (('user', 'stock'),)

class TradeRecord(models.Model):
    record_id = models.AutoField(db_column='Record_id', primary_key=True)  # Field name made lowercase.
    trade_price = models.IntegerField(db_column='Trade_price')  # Field name made lowercase.
    trade_quantity = models.IntegerField(db_column='Trade_quantity')  # Field name made lowercase.
    trade_type = models.CharField(db_column='Trade_type', max_length=1)  # Field name made lowercase.
    trade_date = models.DateTimeField(db_column='Trade_date')  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    stock = models.ForeignKey(Stock, models.DO_NOTHING, db_column='Stock_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'trade_record'
        
class User(models.Model):
    user_id = models.AutoField(db_column='User_id', primary_key=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=30)  # Field name made lowercase.
    nickname = models.CharField(db_column='Nickname', unique=True, max_length=30)  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone_number', unique=True, max_length=30)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'user'