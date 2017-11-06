# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('token', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('to_url', models.CharField(max_length=256)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
