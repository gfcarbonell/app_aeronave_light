# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-30 19:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pilotos', '0005_auto_20161130_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piloto',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargos.Cargo', verbose_name='Cargo - Grado'),
        ),
    ]
