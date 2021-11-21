from django.db import models
from django.utils import timezone
# Create your models here.

# python manage.py inspectdb > models.py 
# DB에 연동한 테이블을 불러올 수 있음
class Stock(models.Model):
    stock_id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=20)
    # price_now = models.IntegerField()
    last_update = models.DateTimeField()
    
    def __str__(self):
        return f'{self.name}: {self.price_now}'

class Comment(models.Model):
    post_id = models.IntegerField(primary_key=True, null=False)
    content = models.TextField()
    create_time = models.DateTimeField()
    stock_id = models.ForeignKey("Stock", related_name="stock", on_delete=models.CASCADE, db_column="Stock_id")

    def __str__(self):
        return f'{self.post_id} : {self.content}'

class User(models.Model):
    user_id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name}: {self.age}'

class Interested_in(models.Model):
    user_id = models.ForeignKey("User", related_name="User", on_delete=models.CASCADE, db_column="User_id")
    stock_id = models.ForeignKey("Stock", related_name="Stock", on_delete=models.CASCADE, db_column="Stock_id")

    def __str__(self):
        return f'{self.user_id}: {self.stock_id}'
