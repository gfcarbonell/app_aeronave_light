# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-30 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='numero_documento_identificacion',
            new_name='dni',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='documento_identificacion',
        ),
        migrations.AlterField(
            model_name='empleado',
            name='descripcion',
            field=models.TextField(blank=True, help_text='(Opcional).', null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='observacion',
            field=models.TextField(blank=True, help_text='(Opcional).', null=True, verbose_name='Observación'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='tipo_empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipos_empleados.TipoEmpleado', verbose_name='Tipo especialista'),
        ),
    ]