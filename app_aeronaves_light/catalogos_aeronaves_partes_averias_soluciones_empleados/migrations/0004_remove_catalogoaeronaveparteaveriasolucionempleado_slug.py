# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 14:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos_aeronaves_partes_averias_soluciones_empleados', '0003_remove_catalogoaeronaveparteaveriasolucionempleado_seleccionar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogoaeronaveparteaveriasolucionempleado',
            name='slug',
        ),
    ]
