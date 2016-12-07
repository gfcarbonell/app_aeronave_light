# -*- encoding: utf-8 -*-
from django.conf import settings
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets
from django.db.models import Q
import socket
from pure_pagination.mixins import PaginationMixin
from django.template.defaultfilters import slugify

from infos_sistemas.mixins import TipoPerfilUsuarioMixin
from .models import CatalogoAeronaveParteAveriaEmpleado


class DiagnosticoAeronaveAveriaEmpleado(CreateView):
    template_name = 'diagnostico_aeronave.html'
    model         = CatalogoAeronaveParteAveriaEmpleado
 

    