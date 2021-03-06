# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 22:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marcas', '0003_auto_20161129_1552'),
        ('modelos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aeronave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotografia', models.ImageField(blank=True, default='default/No_Avatar_1.png', help_text='Subir fotografia (Opcional).', null=True, upload_to='fotografias_aviones', verbose_name='Avatar (Fotografía)')),
                ('descripcion', models.TextField(blank=True, help_text='(Opcional).', null=True, verbose_name='Descripción (Aeronave)')),
                ('activo', models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=True)),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marcas.Marca')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelos.Modelo')),
            ],
            options={
                'verbose_name': 'Aeronave',
                'db_table': 'Aeronaves',
                'ordering': ('tipo_aeronave', 'marca', 'modelo'),
                'verbose_name_plural': 'Aeronaves',
            },
        ),
    ]
