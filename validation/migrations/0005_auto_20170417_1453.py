# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-04-17 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validation', '0004_auto_20161007_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='exclude_keywords',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='query',
            name='include_keywords',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='query',
            name='gender',
            field=models.CharField(blank=True, choices=[(None, 'SELECT'), ('Male', 'Male'), ('Female', 'Female'), ('All', 'All')], max_length=6, null=True),
        ),
    ]
