# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^parte/averia/$', views.CatalogoAeronaveParteAveriaControlListView.as_view(), name='control'),
    url(r'^parte/averia/(?P<search_registro>[-\w\W\d]+)/$', views.CatalogoAeronaveParteAveriaControlListView.as_view(), name='control'),
]
