# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-21 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('last_dt', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u66f4\u65b0\u65f6\u95f4')),
                ('account', models.CharField(max_length=64, verbose_name='\u8d26\u53f7')),
                ('password', models.CharField(max_length=64, verbose_name='\u5bc6\u7801')),
                ('nickname', models.CharField(max_length=64, verbose_name='\u6635\u79f0')),
                ('power', models.IntegerField(choices=[(0, '\u666e\u901a\u7528\u6237'), (1, '\u7279\u7ea6\u7528\u6237'), (2, '\u5c01\u7981\u7528\u6237')], default=0, verbose_name='\u6743\u9650')),
            ],
            options={
                'ordering': ['-create_dt'],
                'abstract': False,
                'verbose_name_plural': '\u7528\u6237',
                'db_table': 'tb_user',
                'verbose_name': '\u7528\u6237',
            },
        ),
    ]
