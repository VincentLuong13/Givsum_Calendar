# Generated by Django 2.0.4 on 2018-04-24 01:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0003_auto_20180423_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 4, 23, 18, 44, 58, 914158)),
        ),
        migrations.AlterField(
            model_name='event',
            name='day_name',
            field=models.IntegerField(default=0),
        ),
    ]