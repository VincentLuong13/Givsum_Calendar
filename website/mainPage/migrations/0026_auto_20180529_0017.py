# Generated by Django 2.0.5 on 2018-05-29 07:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0025_auto_20180527_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 29, 0, 17, 6, 577415)),
        ),
        migrations.AlterField(
            model_name='event',
            name='day_name',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 29, 0, 17, 6, 577415)),
        ),
        migrations.AlterField(
            model_name='eventrepeat',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 29, 0, 17, 6, 577415)),
        ),
        migrations.AlterField(
            model_name='eventrepeat',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 29, 0, 17, 6, 577415)),
        ),
    ]
