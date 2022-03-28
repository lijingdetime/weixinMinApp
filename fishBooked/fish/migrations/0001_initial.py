# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-12 03:50
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=20)),
                ('province', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('detail', models.CharField(blank=True, max_length=100, null=True)),
                ('create_time', models.DateTimeField(default=datetime.datetime(2017, 10, 12, 11, 50, 52, 630658))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '账户信息',
                'verbose_name_plural': '账户信息',
                'db_table': 'account_user_address',
            },
        ),
        migrations.CreateModel(
            name='CheckboxItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('value', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name': 'checkbox复选框',
                'verbose_name_plural': 'checkbox复选框',
            },
        ),
        migrations.CreateModel(
            name='ImageItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(default='', max_length=100)),
                ('image_select', models.ImageField(upload_to='images/%Y/%m/%d')),
            ],
            options={
                'verbose_name': '图片集合',
                'verbose_name_plural': '图片集合',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit1', models.CharField(default='', max_length=100)),
                ('submit2', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('submit3', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('submit4', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('submit5', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('submit6', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('submit7', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('submit8', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('submit9', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('submit10', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('submit11', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('submit12', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('submit13', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('submit14', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('submit15', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('submit16', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('submit17', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('submit18', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('submit19', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('submit20', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('SubmitUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户提交的表单',
                'verbose_name_plural': '用户提交的表单',
            },
        ),
        migrations.CreateModel(
            name='PickerItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name': 'picker选择器',
                'verbose_name_plural': 'picker选择器',
            },
        ),
        migrations.CreateModel(
            name='ProductAbstract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('centent', models.TextField(max_length=1000)),
                ('explaintext', models.TextField(blank=True, help_text='为了给用户提示信息的，这应该在文末，并且管理端填写', null=True)),
                ('ManagerUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('headImage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fish.ImageItems')),
            ],
            options={
                'verbose_name': '商品介绍',
                'verbose_name_plural': '商品介绍',
            },
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('text', 'textType'), ('textarea', 'textareaType'), ('picker', 'pickerType'), ('radio', 'radioType'), ('explain', 'explainType'), ('image', 'imageType'), ('checkbox', 'checkboxType')], max_length=100)),
                ('name', models.CharField(blank=True, help_text='起排序作用的，起名叫name是为了对应小程序中属性名称', max_length=100, null=True)),
                ('placeholder', models.CharField(blank=True, help_text='text,textarea类的才有这个属性', max_length=300, null=True)),
                ('prompt', models.CharField(blank=True, help_text='就是提示这个选择是用来干嘛的，总不能一堆空白让人选呀，text和textarea好歹还有placeholder用来提示', max_length=300, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fish.ProductAbstract')),
            ],
            options={
                'verbose_name': '商品内部页面',
                'verbose_name_plural': '商品内部页面',
            },
        ),
        migrations.CreateModel(
            name='RadioItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('value', models.CharField(default='', max_length=100)),
                ('ProductDetail', models.ForeignKey(blank=True, help_text='关联radio选项需要的name和value', null=True, on_delete=django.db.models.deletion.CASCADE, to='fish.ProductDetail')),
            ],
            options={
                'verbose_name': 'radio单选框',
                'verbose_name_plural': 'radio单选框',
            },
        ),
        migrations.CreateModel(
            name='ZoneSelect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='区的名称，比如“长安大学渭水校区”用于做区分', max_length=100)),
                ('x_coordinate', models.FloatField(blank=True, help_text='横坐标', null=True)),
                ('y_coordinate', models.FloatField(blank=True, help_text='纵坐标', null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'verbose_name': '位置',
                'verbose_name_plural': '位置',
            },
        ),
        migrations.AddField(
            model_name='pickeritems',
            name='ProductDetail',
            field=models.ForeignKey(blank=True, help_text='关联picker选项需要array数组，是一组value', null=True, on_delete=django.db.models.deletion.CASCADE, to='fish.ProductDetail'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fish.ProductAbstract'),
        ),
        migrations.AddField(
            model_name='imageitems',
            name='ProductAbstract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fish.ProductAbstract'),
        ),
        migrations.AddField(
            model_name='checkboxitems',
            name='ProductDetail',
            field=models.ForeignKey(blank=True, help_text='关联checkbox选项需要的name和value', null=True, on_delete=django.db.models.deletion.CASCADE, to='fish.ProductDetail'),
        ),
        migrations.AlterUniqueTogether(
            name='productdetail',
            unique_together=set([('product', 'name')]),
        ),
    ]
