# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-09 12:05
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fish', '0010_auto_20171109_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformationAdd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='电话号码')),
                ('really_name', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='姓名')),
                ('address', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='住址')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '管理员用户更多的信息',
                'verbose_name_plural': '管理员用户更多的信息',
            },
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 9, 20, 5, 44, 554984)),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 9, 20, 5, 44, 567999), null=True),
        ),
        migrations.AlterField(
            model_name='orderimage',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 9, 20, 5, 44, 571994), null=True),
        ),
    ]
