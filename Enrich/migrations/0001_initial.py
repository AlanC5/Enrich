# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
            ('user', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization_Staff',
            fields=[
                ('organization_staff_id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('organization_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('review_id', models.IntegerField(primary_key=True, serialize=False)),
                ('review_text', models.TextField()),
                ('rating', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('user_id', models.IntegerField()),
                ('organization_id', models.IntegerField()),
            ],
        ),
    ]
