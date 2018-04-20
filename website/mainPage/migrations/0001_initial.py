# Generated by Django 2.0.4 on 2018-04-20 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('time', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
                ('event_description', models.CharField(default='', max_length=750)),
                ('address', models.CharField(default='', max_length=750)),
                ('picture_url', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('members', models.IntegerField(default=0)),
                ('website', models.CharField(max_length=1000)),
            ],
        ),
    ]
