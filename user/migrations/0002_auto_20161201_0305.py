# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
