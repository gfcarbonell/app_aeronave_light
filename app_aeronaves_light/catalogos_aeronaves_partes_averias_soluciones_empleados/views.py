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

from django.http import JsonResponse


class CatalogoAeronaveParteAveriaSolucionListView(TipoPerfilUsuarioMixin, AccessLoginRequiredMixin, ListView):
    template_name = 'diagnostico_aeronave.html'
    model         = CatalogoAeronaveParteAveriaSolucion
    success_url   = reverse_lazy('diagnostico_aeronave:control')

    def get_context_data(self, **kwarg):
        context  = super(CatalogoAeronaveParteAveriaSolucionListView, self).get_context_data(**kwarg)
        aeronaves = Aeronave.objects.all()
        data = {
            'aeronaves'    : aeronaves,
        }
        context.update(data)
        return context

    def get(self, request, *args, **kwargs):
        if  request.GET.get('format', None)=='api' and request.GET.get('aeronave', None) :
               return self.catalogo_json(request.GET.get('aeronave', None))
        if  request.GET.get('format', None)=='api' and request.GET.get('averia', None) :
               return self.catalogo_soluciones(request.GET.get('averia', None))
        else:
            return super(CatalogoAeronaveParteAveriaSolucionListView, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        if self.request.GET.get('aeronave', None):
            aeronave = self.request.GET.get('aeronave', None)
            queryset = CatalogoAeronaveParteAveriaSolucion.objects.filter(
                Q(catalogo_aeronave_parte_averia__catalogo_aeronave_parte__aeronave=aeronave)
            )
        else:
            queryset = super(CatalogoAeronaveParteAveriaSolucionListView, self).get_queryset()
        return queryset  

    def empleado_json(self, tipo_empleado):
        data = [{
            'id': empleado.id,
            'tipo_empleado': empleado.tipo_empleado.nombre,
            'nombre': empleado.nombre,
        }for empleado in Empleado.objects.filter(tipo_empleado=tipo_empleado).order_by('id')]
        return JsonResponse(data, safe=False)

    def catalogo_averias(self, aeronave):
        data = [{
                    'id' :catalogo.averia.id,
                    'nombre' :catalogo.averia.nombre
        }for catalogo in CatalogoAeronaveParteAveria.objects.filter(
                Q(catalogo_aeronave_parte__aeronave=aeronave)
            )]
        return JsonResponse(data, safe=False)  


    def catalogo_json(self, aeronave):
        data = [{
            'id': catalogo.id,
            'catalogo_aeronave_parte_averia': {
                            'id'                     :catalogo.catalogo_aeronave_parte_averia.id,
                            'catalogo_aeronave_parte':{
                                                            'id': catalogo.catalogo_aeronave_parte_averia.catalogo_aeronave_parte.id,
                                                            'ubicacion': catalogo.catalogo_aeronave_parte_averia.catalogo_aeronave_parte.ubicacion,
                                                      },
                            'averia': {
                                        'id' :catalogo.catalogo_aeronave_parte_averia.averia.id,
                                        'nombre' :catalogo.catalogo_aeronave_parte_averia.averia.nombre
                                    }, 
                            'descripcion': catalogo.catalogo_aeronave_parte_averia.descripcion
                        },
            'solucion': {
                            'id'           : catalogo.solucion.id,
                            'nombre'       : catalogo.solucion.nombre,
                            'tipo_empleado': {
                                                'id'    : catalogo.solucion.tipo_empleado.id,
                                                'nombre':catalogo.solucion.tipo_empleado.nombre
                                             }
                        },
            'descripcion': catalogo.descripcion,

        }for catalogo in CatalogoAeronaveParteAveriaSolucion.objects.filter(
                Q(catalogo_aeronave_parte_averia__catalogo_aeronave_parte__aeronave=aeronave)
            )]
        return JsonResponse(data, safe=False)   
                
    def catalogo_soluciones(self, averia):
        data = [{
                    'averia': {
                                'id' :catalogo.catalogo_aeronave_parte_averia.averia.id,
                                'nombre' :catalogo.catalogo_aeronave_parte_averia.averia.nombre
                             }, 
                    'solucion': {
                                'id'           : catalogo.solucion.id,
                                'nombre'       : catalogo.solucion.nombre,
                                'tipo_empleado': {
                                                    'id'    : catalogo.solucion.tipo_empleado.id,
                                                    'nombre':catalogo.solucion.tipo_empleado.nombre
                                                 }
                             }, 
                
        }for catalogo in CatalogoAeronaveParteAveriaSolucion.objects.filter(
                Q(catalogo_aeronave_parte_averia__averia=averia)
            )]
        return JsonResponse(data, safe=False)            

