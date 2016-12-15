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
from django.http import HttpResponse, HttpResponseBadRequest
import json
from django.views.generic.edit import FormMixin


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
        if  request.GET.get('format', None)=='api' and request.GET.get('aeronave', None) and request.GET.get('averia', None) :
               return self.catalogo_final_json(request.GET.get('aeronave', None), request.GET.get('averia', None))
        if  request.GET.get('format', None)=='api' and request.GET.get('aeronave', None) :
               return self.catalogo_json(request.GET.get('aeronave', None))
        if  request.GET.get('format', None)=='api' and request.GET.get('averia', None) :
               return self.catalogo_soluciones(request.GET.get('averia', None))
        if  request.GET.get('format', None)=='api' and request.GET.get('tipo_empleado', None) :
               return self.empleado_json(request.GET.get('tipo_empleado', None))
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
            'id_tipo_empleado': empleado.tipo_empleado.id,
            'tipo_empleado'   : empleado.tipo_empleado.nombre,
            'apellido_paterno': empleado.apellido_paterno,
            'apellido_materno': empleado.apellido_materno,
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


    def catalogo_final_json(self, aeronave, averia):
        data = [{
            'id': catalogo.id,
        }for catalogo in CatalogoAeronaveParteAveriaSolucion.objects.filter(
                Q(catalogo_aeronave_parte_averia__catalogo_aeronave_parte__aeronave=aeronave) & 
                Q(catalogo_aeronave_parte_averia__averia=averia) 
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


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return self.render_to_json_response(data)
        else:
            return response


class DiagnosticarCreateView(TipoPerfilUsuarioMixin, AccessLoginRequiredMixin, CreateView):
    model         = CatalogoAeronaveParteAveriaSolucionEmpleado
    success_url   = reverse_lazy('aeronave:control')


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import StreamingHttpResponse
from django.db import connection
from datetime import datetime

@csrf_exempt
def view_ajax(request):
    if request.method == 'POST':
        json_str=((request.body).decode('utf-8'))
        json_obj=json.loads(json_str)

        empleado = Empleado.objects.get(id=int(json_obj["empleado"]))
        cat = CatalogoAeronaveParteAveriaSolucion.objects.get(id=int(json_obj["catalogo_aeronave_parte_averia"]))
        fecha_diagnostico = json_obj["fecha_diagnostico"]
        seleccionar = json_obj["seleccionar"]
        
        catalogo = CatalogoAeronaveParteAveriaSolucionEmpleado(
            empleado = empleado,
            catalogos_aeronaves_partes_averias_soluciones = cat,
            fecha_diagnostico = fecha_diagnostico,
            seleccionar = seleccionar 
        )
        catalogo.save()
       
        return StreamingHttpResponse('it was post request: '+str(json_obj))
    return StreamingHttpResponse('it was GET request')



