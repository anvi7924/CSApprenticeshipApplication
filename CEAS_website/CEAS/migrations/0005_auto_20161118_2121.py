# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-18 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CEAS', '0004_auto_20161118_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='fifthChoice',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='fourthChoice',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='secondChoice',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='thirdChoice',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='studentproject',
            name='project_id',
            field=models.IntegerField(null=True),
        ),
    ]
