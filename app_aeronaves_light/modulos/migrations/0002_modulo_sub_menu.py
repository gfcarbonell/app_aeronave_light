# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-22 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modulos', '0001_initial'),
        ('sub_menus', '0001_initial'),
        ('catalogos_modulos_menus_sub_menus', '0005_catalogomodulomenusubmenu_sub_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulo',
            name='sub_menu',
            field=models.ManyToManyField(through='catalogos_modulos_menus_sub_menus.CatalogoModuloMenuSubMenu', to='sub_menus.SubMenu'),
        ),
    ]
