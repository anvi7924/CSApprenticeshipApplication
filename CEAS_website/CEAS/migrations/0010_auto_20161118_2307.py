# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-18 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CEAS', '0009_auto_20161118_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]
