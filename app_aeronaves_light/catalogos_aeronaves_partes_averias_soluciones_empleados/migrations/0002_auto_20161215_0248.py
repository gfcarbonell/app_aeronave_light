# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 07:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos_aeronaves_partes_averias_soluciones_empleados', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalogoaeronaveparteaveriasolucionempleado',
            old_name='selecionar',
            new_name='seleccionar',
        ),
    ]
