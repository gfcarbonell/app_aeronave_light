# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-22 17:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paises', '0001_initial'),
        ('departamentos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamento',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paises.Pais'),
        ),
    ]