# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-29 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aeronaves', '0001_initial'),
        ('catalogos_aeronaves_partes', '0001_initial'),
        ('partes_aeronaves', '0003_auto_20161129_1552'),
        ('tipos_aeronaves', '0003_auto_20161129_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='aeronave',
            name='parte_aeronave',
            field=models.ManyToManyField(default=None, null=True, through='catalogos_aeronaves_partes.CatalogoAeronaveParte', to='partes_aeronaves.ParteAeronave'),
        ),
        migrations.AddField(
            model_name='aeronave',
            name='tipo_aeronave',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipos_aeronaves.TipoAeronave'),
        ),
    ]
