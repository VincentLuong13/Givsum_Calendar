# Generated by Django 2.0.4 on 2018-04-23 23:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
        migrations.AddField(
            model_name='event',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 4, 23, 16, 8, 49, 956699)),
        ),
        migrations.AddField(
            model_name='event',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='event_url',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AlterField(
            model_name='event',
            name='picture_url',
            field=models.CharField(default='', max_length=3000),
        ),
    ]
