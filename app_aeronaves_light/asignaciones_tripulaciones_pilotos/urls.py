# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
  url(r'^tripulacion/nuevo/$', views.AsignacionTripulacionPilotoCreateView.as_view(), name='create'),
]
