# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 22:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogos_aeronaves_partes', '0001_initial'),
        ('averias', '0003_auto_20161129_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogoAeronaveParteAveria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, help_text='(Opcional)', null=True, verbose_name='Descripción')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('averia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='averias.Averia')),
                ('catalogo_aeronave_parte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos_aeronaves_partes.CatalogoAeronaveParte')),
            ],
            options={
                'verbose_name': 'Catalogo Aeronave Parte Averia',
                'db_table': 'Catalogos_Aeronaves_Partes_Averias',
                'verbose_name_plural': 'Catalogos Aeronaves Partes Averias',
            },
        ),
    ]
