# Generated by Django 3.1.6 on 2021-02-10 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20210210_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 10, 11, 5, 21, 133785)),
        ),
    ]