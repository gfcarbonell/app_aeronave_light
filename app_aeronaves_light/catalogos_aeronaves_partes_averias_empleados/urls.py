# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^diagnostico/nuevo/$', views.DiagnosticoAeronaveAveriaEmpleado.as_view(), name='create'),
 ]