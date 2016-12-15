# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^orden-vuelo/nuevo/$', views.OrdenVueloCreateView.as_view(), name='create'),
    url(r'^orden-vuelo/(?P<slug>[-\w\W\d]+)/modificar/$', views.OrdenVueloUpdateView.as_view(), name='update'),
    url(r'^orden-vuelo/(?P<slug>[-\w\W\d]+)/$', views.OrdenVueloDetailView.as_view(), name='detail'),
    url(r'^ordenes-de-vuelos/$', views.OrdenVueloControlListView.as_view(), name='control'),
    url(r'^ordenes-de-vuelos/(?P<search_registro>[-\w\W\d]+)/$', views.OrdenVueloControlListView.as_view(), name='control'),
]
