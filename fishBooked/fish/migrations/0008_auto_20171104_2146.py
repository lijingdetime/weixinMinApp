# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-04 13:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fish', '0007_auto_20171104_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 4, 21, 46, 58, 225887)),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 4, 21, 46, 58, 232893), null=True),
        ),
    ]
