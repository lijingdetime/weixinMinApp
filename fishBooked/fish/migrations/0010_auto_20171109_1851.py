# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-09 10:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fish', '0009_auto_20171109_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 9, 18, 51, 59, 76955)),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 9, 18, 51, 59, 83459), null=True),
        ),
        migrations.AlterField(
            model_name='orderimage',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 9, 18, 51, 59, 85460), null=True),
        ),
    ]
