# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-29 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aeronaves', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogoAeronaveParte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden_aeronave', models.SmallIntegerField(default=0)),
                ('orden_parte_aeronave', models.SmallIntegerField(default=0)),
                ('imagen', models.ImageField(blank=True, help_text='Subir imagen. (Opcional)', null=True, upload_to='')),
                ('descripcion', models.TextField(blank=True, help_text='(Opcional)', null=True, verbose_name='Observación')),
                ('observacion', models.TextField(blank=True, help_text='(Opcional)', null=True, verbose_name='Descripción')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('aeronave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aeronaves.Aeronave')),
            ],
            options={
                'verbose_name': 'Catalogo Aeronave Parte',
                'verbose_name_plural': 'Catalogos Aeronaves Partes',
                'ordering': ('orden_aeronave', 'orden_parte_aeronave'),
                'db_table': 'Catalogos_Aeronaves_Partes',
            },
        ),
    ]