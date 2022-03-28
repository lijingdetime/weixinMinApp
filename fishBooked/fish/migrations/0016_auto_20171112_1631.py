# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-12 08:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fish', '0015_auto_20171112_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertising',
            name='Product',
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 12, 16, 31, 56, 152015)),
        ),
        migrations.AlterField(
            model_name='advertisinginfo',
            name='advertiser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fish.ProductAbstract'),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 12, 16, 31, 56, 164017), null=True),
        ),
        migrations.AlterField(
            model_name='orderimage',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 12, 16, 31, 56, 166020), null=True),
        ),
        migrations.DeleteModel(
            name='advertising',
        ),
    ]
