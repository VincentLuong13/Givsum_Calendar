# Generated by Django 2.0.5 on 2018-05-28 06:05

import datetime
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0023_auto_20180527_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 27, 23, 5, 16, 749814)),
        ),
        migrations.AlterField(
            model_name='event',
            name='day_repeat',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('None', 'None'), (1, 'Sunday'), (2, 'Monday'), (3, 'Tuesday'), (4, 'Wednesday'), (5, 'Thursday'), (6, 'Friday'), (7, 'Saturday')], default='None', max_length=18),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 27, 23, 5, 16, 749814)),
        ),
        migrations.AlterField(
            model_name='eventrepeat',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 27, 23, 5, 16, 750810)),
        ),
        migrations.AlterField(
            model_name='eventrepeat',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 27, 23, 5, 16, 750810)),
        ),
    ]
