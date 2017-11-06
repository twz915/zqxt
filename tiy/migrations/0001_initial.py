# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tutorial.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadStatistic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('download_url', models.CharField(max_length=512, verbose_name='\u4e0b\u8f7d\u94fe\u63a5', db_index=True)),
                ('count', models.PositiveIntegerField(verbose_name='\u4e0b\u8f7d\u6b21\u6570')),
            ],
            options={
                'verbose_name': '\u4e0b\u8f7d\u7edf\u8ba1',
                'verbose_name_plural': '\u4e0b\u8f7d\u7edf\u8ba1',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u540d\u79f0', db_index=True)),
                ('column', models.CharField(max_length=100, null=True, verbose_name='\u680f\u76ee', blank=True)),
                ('code', tutorial.fields.CompressedTextField(null=True, verbose_name='\u4ee3\u7801', blank=True)),
                ('result', tutorial.fields.CompressedTextField(null=True, verbose_name='\u7ed3\u679c', blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', null=True)),
            ],
            options={
                'verbose_name': '\u5b9e\u4f8b',
                'verbose_name_plural': '\u5b9e\u4f8b',
            },
            bases=(models.Model,),
        ),
    ]
