# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-29 20:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distritos', '0003_auto_20161122_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distrito',
            name='direccion_ip',
        ),
        migrations.RemoveField(
            model_name='distrito',
            name='fecha_registro',
        ),
        migrations.RemoveField(
            model_name='distrito',
            name='fecha_ultima_actualizacion',
        ),
        migrations.RemoveField(
            model_name='distrito',
            name='nombre_host',
        ),
        migrations.RemoveField(
            model_name='distrito',
            name='ultimo_direccion_ip',
        ),
        migrations.RemoveField(
            model_name='distrito',
            name='ultimo_nombre_host',
        ),
        migrations.RemoveField(
            model_name='distrito',
            name='ultimo_usuario_editor',
        ),
        migrations.RemoveField(
            model_name='distrito',
            name='usuario_creador',
        ),
    ]
