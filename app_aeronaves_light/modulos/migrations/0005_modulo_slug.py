# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-30 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0004_auto_20161129_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulo',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]