# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-30 18:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pilotos', '0003_auto_20161130_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='piloto',
            name='observacion',
        ),
    ]
