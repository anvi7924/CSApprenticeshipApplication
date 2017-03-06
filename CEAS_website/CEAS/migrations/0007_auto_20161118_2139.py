# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-18 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CEAS', '0006_auto_20161118_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='backcheck',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Do not know', 'Do not know')], default='Yes', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='dhtraining',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Do not know', 'Do not know')], default='Yes', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='fifthChoice',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='firstChoice',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='fourthChoice',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='secondChoice',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='thirdChoice',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]