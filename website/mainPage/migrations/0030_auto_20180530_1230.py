# Generated by Django 2.0.5 on 2018-05-30 19:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0029_auto_20180530_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventrepeat',
            name='end_date',
        ),
        migrations.AddField(
            model_name='eventrepeat',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 30, 12, 30, 19, 488915)),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 30, 12, 30, 19, 488915)),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 30, 12, 30, 19, 488915)),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 30, 12, 30, 19, 488915)),
        ),
        migrations.AlterField(
            model_name='eventrepeat',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 30, 12, 30, 19, 488915)),
        ),
    ]