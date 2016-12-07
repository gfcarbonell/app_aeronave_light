# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogos_aeronaves_partes_averias_soluciones', '0001_initial'),
        ('soluciones', '0003_auto_20161207_1727'),
        ('catalogos_aeronaves_partes_averias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogoaeronaveparteaveria',
            name='solucion',
            field=models.ManyToManyField(through='catalogos_aeronaves_partes_averias_soluciones.CatalogoAeronaveParteAveriaSolucion', to='soluciones.Solucion'),
        ),
    ]