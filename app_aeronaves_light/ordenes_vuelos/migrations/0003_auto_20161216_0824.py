# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes_vuelos', '0002_auto_20161215_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenvuelo',
            name='fecha_vuelo',
            field=models.DateTimeField(),
        ),
    ]
