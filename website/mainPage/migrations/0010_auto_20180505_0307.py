# Generated by Django 2.0.4 on 2018-05-05 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0009_auto_20180505_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 5, 3, 7, 33, 983796)),
        ),
    ]
