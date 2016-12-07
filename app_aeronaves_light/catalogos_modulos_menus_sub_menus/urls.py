# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^modulos/$', views.CatalagoModuloMenuTemplateView.as_view(), name='main'),
    url(r'^mantenimiento/$', views.MantenimientoAeronaveTemplateView.as_view(), name='mantenimiento_aeronave'),
    url(r'^mantenimiento/menu/$', views.MantenimientoAeronaveMenuTemplateView.as_view(), name='mantenimiento_aeronave_menu'),
]
