# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-29 20:05
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentoIdentificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_index=True, help_text='Escribir el nombre del documento de Identificación.', max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)])),
                ('siglas', models.CharField(db_index=True, max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(10)])),
                ('numero_digito', models.PositiveSmallIntegerField(help_text='Ingresar el número de dígitos total del documento de indetificación.', verbose_name='Número dígito(s)')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
            ],
            options={
                'ordering': ('nombre',),
                'verbose_name': 'Documento Identificación',
                'db_table': 'Documentos_Identificaciones',
                'verbose_name_plural': 'Documentos Identificaciones',
            },
        ),
    ]
