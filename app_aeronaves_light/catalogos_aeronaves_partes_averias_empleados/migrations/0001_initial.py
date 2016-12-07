# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-29 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogos_aeronaves_partes_averias', '0001_initial'),
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogoAeronaveParteAveriaEmpleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, help_text='(Opcional)', null=True, verbose_name='Observación')),
                ('observacion', models.TextField(blank=True, help_text='(Opcional)', null=True, verbose_name='Descripción')),
                ('seleccionar', models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=True)),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('catalogos_aeronaves_partes_averias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos_aeronaves_partes_averias.CatalogoAeronaveParteAveria')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.Empleado')),
            ],
            options={
                'verbose_name': 'Catalogo Aeronave Parte Averias Empleado',
                'verbose_name_plural': 'Catalogos Aeronaves Partes Averias Empleado',
                'db_table': 'Catalogos_Aeronaves_Partes_Averias_Empleado',
            },
        ),
    ]