# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-29 20:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marcas', '0002_auto_20161122_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marca',
            name='direccion_ip',
        ),
        migrations.RemoveField(
            model_name='marca',
            name='fecha_registro',
        ),
        migrations.RemoveField(
            model_name='marca',
            name='fecha_ultima_actualizacion',
        ),
        migrations.RemoveField(
            model_name='marca',
            name='nombre_host',
        ),
        migrations.RemoveField(
            model_name='marca',
            name='ultimo_direccion_ip',
        ),
        migrations.RemoveField(
            model_name='marca',
            name='ultimo_nombre_host',
        ),
        migrations.RemoveField(
            model_name='marca',
            name='ultimo_usuario_editor',
        ),
        migrations.RemoveField(
            model_name='marca',
            name='usuario_creador',
        ),
    ]
