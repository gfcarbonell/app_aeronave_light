# -*- encoding: utf-8 -*-
from django.conf import settings
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets
from django.db.models import Q
import socket
from pure_pagination.mixins import PaginationMixin
from django.template.defaultfilters import slugify
from .models import CatalogoAeronaveParteAveriaSolucionEmpleado
from .forms import CatalogoAeronaveParteAveriaSolucionEmpleadoModelForm
from infos_sistemas.mixins import TipoPerfilUsuarioMixin, AccessLoginRequiredMixin
from aeronaves.models import Aeronave
from catalogos_aeronaves_partes_averias.models import CatalogoAeronaveParteAveria
from catalogos_aeronaves_partes_averias_soluciones.models import CatalogoAeronaveParteAveriaSolucion
from empleados.models import Empleado

class CatalogoAeronaveParteAveriaSolucionEmpleadoCreateView(TipoPerfilUsuarioMixin, AccessLoginRequiredMixin, CreateView):
    template_name = 'diagnostico_aeronave.html'
    form_class    = CatalogoAeronaveParteAveriaSolucionEmpleadoModelForm
    model         = CatalogoAeronaveParteAveriaSolucionEmpleado
    success_url   = reverse_lazy('diagnostico_aeronave:control')

    def get_context_data(self, **kwarg):
        context  = super(CatalogoAeronaveParteAveriaSolucionEmpleadoCreateView, self).get_context_data(**kwarg)
        aeronaves = Aeronave.objects.all()
        catalogos_aeronaves_partes = CatalogoAeronaveParteAveria.objects.filter(
                catalogo_aeronave_parte__aeronave = 1
            )
        catalogos_aeronaves_partes_soluciones = CatalogoAeronaveParteAveriaSolucion.objects.filter(
                catalogo_aeronave_parte_averia__catalogo_aeronave_parte__aeronave = 1
            )
        
        soluciones = CatalogoAeronaveParteAveriaSolucion.objects.filter(
                catalogo_aeronave_parte_averia__catalogo_aeronave_parte__aeronave = 1, 
                catalogo_aeronave_parte_averia__solucion__tipo_empleado = 1 
            )

        empleados = Empleado.objects.filter(
                tipo_empleado = 1
            )
        data = {
            'aeronaves'                            : aeronaves,
            'catalogos_aeronaves_partes'           : catalogos_aeronaves_partes,
            'catalogos_aeronaves_partes_soluciones': catalogos_aeronaves_partes_soluciones,
            'empleados'                            : empleados,

        }

        context.update(data)
        return context
