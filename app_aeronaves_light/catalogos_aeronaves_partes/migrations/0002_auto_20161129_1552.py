# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-29 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogos_aeronaves_partes', '0001_initial'),
        ('catalogos_aeronaves_partes_averias', '0001_initial'),
        ('averias', '0003_auto_20161129_1552'),
        ('partes_aeronaves', '0003_auto_20161129_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogoaeronaveparte',
            name='averia',
            field=models.ManyToManyField(through='catalogos_aeronaves_partes_averias.CatalogoAeronaveParteAveria', to='averias.Averia'),
        ),
        migrations.AddField(
            model_name='catalogoaeronaveparte',
            name='parte_aeronave',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partes_aeronaves.ParteAeronave'),
        ),
    ]
