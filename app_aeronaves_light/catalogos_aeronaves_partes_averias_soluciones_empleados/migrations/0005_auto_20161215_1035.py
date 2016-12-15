# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 15:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos_aeronaves_partes_averias_soluciones_empleados', '0004_remove_catalogoaeronaveparteaveriasolucionempleado_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogoaeronaveparteaveriasolucionempleado',
            name='fecha_diagnostico',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 15, 10, 35, 15, 85283)),
        ),
        migrations.AddField(
            model_name='catalogoaeronaveparteaveriasolucionempleado',
            name='seleccionar',
            field=models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=False),
        ),
    ]
