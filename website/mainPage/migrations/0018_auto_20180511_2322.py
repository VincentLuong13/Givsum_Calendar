# Generated by Django 2.0.4 on 2018-05-12 06:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0017_auto_20180505_0355'),
    ]

    operations = [
        migrations.AddField(
            model_name='atendee',
            name='friends',
            field=models.ManyToManyField(related_name='_atendee_friends_+', to='mainPage.Atendee'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 11, 23, 22, 53, 975177)),
        ),
        migrations.AlterField(
            model_name='event',
            name='day_name',
            field=models.IntegerField(default=4),
        ),
    ]
