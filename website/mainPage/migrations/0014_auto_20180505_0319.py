# Generated by Django 2.0.4 on 2018-05-05 10:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0013_auto_20180505_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendee',
            name='events',
            field=models.ManyToManyField(related_name='Atendees', to='mainPage.Event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 5, 3, 19, 56, 708507)),
        ),
    ]
