# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-09 12:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fish', '0011_auto_20171109_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinformationadd',
            name='really_name',
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 9, 20, 11, 10, 391229)),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 9, 20, 11, 10, 397733), null=True),
        ),
        migrations.AlterField(
            model_name='orderimage',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 9, 20, 11, 10, 399735), null=True),
        ),
    ]
