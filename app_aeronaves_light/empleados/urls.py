# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^especialista/nuevo/$', views.EmpleadoCreateView.as_view(), name='create'),
    #url(r'^empleado/(?P<slug>[-\w\W\d]+)/modificar/$', views.EmpleadoUpdateView.as_view(), name='update'),
    url(r'^especialista/(?P<slug>[-\w\W\d]+)/modificar/$', views.EmpleadoUpdateView.as_view(), name='update'),
    url(r'^especialista/(?P<slug>[-\w\W\d]+)/$', views.EmpleadoDetailView.as_view(), name='detail'),
    url(r'^especialistas/$', views.EmpleadoControlListView.as_view(), name='control'),
    url(r'^especialistas/(?P<search_registro>[-\w\W\d]+)/$', views.EmpleadoControlListView.as_view(), name='control'),
]
