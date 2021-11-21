# Generated by Django 3.2.9 on 2021-11-18 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StockInfo', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('User_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('Age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Interested_in',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stock_id', models.ForeignKey(db_column='Stock_id', on_delete=django.db.models.deletion.CASCADE, related_name='Stock', to='StockInfo.stock')),
                ('User_id', models.ForeignKey(db_column='User_id', on_delete=django.db.models.deletion.CASCADE, related_name='User', to='StockInfo.user')),
            ],
        ),
    ]