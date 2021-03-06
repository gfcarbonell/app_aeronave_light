# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-22 17:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cargos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='ultimo_usuario_editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargos_cargo_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cargo',
            name='usuario_creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
