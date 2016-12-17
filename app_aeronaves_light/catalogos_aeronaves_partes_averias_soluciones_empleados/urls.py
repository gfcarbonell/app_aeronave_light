# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^diagnostico/nuevo/$', views.CatalogoAeronaveParteAveriaSolucionListView.as_view(), name='create'),
    url(r'^diagnosticos/$', views.DiagnosticoListView.as_view(), name='list'),
    url(r'^diagnosticos/(?P<search_registro>[-\w\W\d]+)/$', views.DiagnosticoListView.as_view(), name='list'),
    url(r'^diagnostico/create/$', views.view_ajax, name='nuevo'),
]
