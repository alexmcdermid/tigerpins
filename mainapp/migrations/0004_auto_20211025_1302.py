# Generated by Django 3.2.8 on 2021-10-25 13:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20211025_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='pin',
            name='note',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='pin',
            name='purpose',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='pin',
            name='rating',
            field=models.IntegerField(default=5),
        ),
    ]
