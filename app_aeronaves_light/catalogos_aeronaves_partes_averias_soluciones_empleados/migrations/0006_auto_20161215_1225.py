# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 17:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos_aeronaves_partes_averias_soluciones_empleados', '0005_auto_20161215_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogoaeronaveparteaveriasolucionempleado',
            name='fecha_diagnostico',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 15, 12, 25, 1, 709477)),
        ),
    ]
