# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-16 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('organization_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('free', models.BooleanField()),
                ('tuition', models.TextField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('category', models.TextField()),
                ('address', models.TextField()),
            ],
        ),
    ]
