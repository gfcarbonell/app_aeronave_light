# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-29 20:23
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoEmpleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_index=True, help_text='Escribir el nombre del tipo empleado.', max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)])),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Tipo Empleado',
                'ordering': ('nombre',),
                'db_table': 'Tipos_Empleados',
                'verbose_name_plural': 'Tipos Empleados',
            },
        ),
    ]
