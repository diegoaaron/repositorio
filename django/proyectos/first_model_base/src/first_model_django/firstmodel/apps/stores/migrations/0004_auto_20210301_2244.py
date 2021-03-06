# Generated by Django 3.1.7 on 2021-03-01 22:44

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_auto_20210301_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='store',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='date_lastupdated',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='store',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='store',
            name='timestamp_added',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='timestamp_lastupdated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='address',
            field=models.CharField(max_length=30),
        ),
    ]
