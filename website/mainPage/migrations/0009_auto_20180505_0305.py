# Generated by Django 2.0.4 on 2018-05-05 10:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0008_auto_20180505_0304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={},
        ),
        migrations.AlterField(
            model_name='event',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 5, 3, 5, 31, 481134)),
        ),
    ]
