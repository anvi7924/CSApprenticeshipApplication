# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-18 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CEAS', '0007_auto_20161118_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='secondChoice',
            field=models.CharField(blank=True, choices=[('', '')], max_length=50, null=True),
        ),
    ]
