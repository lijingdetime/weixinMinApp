# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-12 05:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fish', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountuser',
            name='zone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 12, 13, 47, 36, 658699)),
        ),
    ]