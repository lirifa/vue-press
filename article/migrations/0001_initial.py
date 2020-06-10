# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-05 07:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_auto_20191104_0405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('last_dt', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u66f4\u65b0\u65f6\u95f4')),
                ('title', models.CharField(max_length=64, verbose_name='\u6807\u9898')),
                ('content', tinymce.models.HTMLField(blank=True, null=True, verbose_name='\u6b63\u6587')),
                ('summary', models.CharField(max_length=256, null=True, verbose_name='\u6458\u8981')),
                ('cover_url', models.CharField(max_length=128, null=True, verbose_name='\u5c01\u9762')),
                ('status', models.IntegerField(default=0, verbose_name='\u72b6\u6001')),
                ('is_top', models.BooleanField(default=False, verbose_name='\u7f6e\u9876')),
                ('reads_count', models.IntegerField(default=0, verbose_name='\u9605\u8bfb\u91cf')),
                ('like_count', models.IntegerField(default=0, verbose_name='\u559c\u6b22\u91cf')),
            ],
            options={
                'ordering': ['-create_dt'],
                'abstract': False,
                'db_table': 'tb_article',
            },
        ),
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('last_dt', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u66f4\u65b0\u65f6\u95f4')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='\u540d\u79f0')),
                ('type', models.IntegerField(choices=[(0, '\u666e\u901a\u6807\u7b7e'), (1, '\u63a8\u8350\u6807\u7b7e')], verbose_name='\u7c7b\u522b')),
            ],
            options={
                'ordering': ['-create_dt'],
                'abstract': False,
                'verbose_name_plural': '\u6807\u7b7e',
                'db_table': 'tb_articletag',
                'verbose_name': '\u6807\u7b7e',
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('last_dt', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u66f4\u65b0\u65f6\u95f4')),
                ('key', models.CharField(max_length=64, unique=True, verbose_name='\u5e73\u53f0\u5173\u952e\u5b57')),
                ('name', models.CharField(max_length=64, verbose_name='\u5e73\u53f0\u540d\u79f0')),
            ],
            options={
                'ordering': ['-create_dt'],
                'abstract': False,
                'db_table': 'tb_platform',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='platform',
            field=models.ManyToManyField(blank=True, to='article.Platform', verbose_name='\u7ec8\u7aef'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='article.ArticleTag', verbose_name='\u6807\u7b7e'),
        ),
        migrations.AddField(
            model_name='article',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='\u6240\u5c5e\u7528\u6237'),
        ),
    ]