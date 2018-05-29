# Generated by Django 2.0.5 on 2018-05-29 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0026_auto_20180529_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventrepeat',
            name='start_date',
        ),
        migrations.AddField(
            model_name='eventrepeat',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 29, 0, 19, 55, 470224)),
        ),
        migrations.AddField(
            model_name='eventrepeat',
            name='name',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 29, 0, 19, 55, 470224)),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 29, 0, 19, 55, 470224)),
        ),
        migrations.AlterField(
            model_name='eventrepeat',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 29, 0, 19, 55, 470224)),
        ),
    ]