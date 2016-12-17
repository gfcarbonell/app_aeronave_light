# -*- encoding: utf-8 -*-
from django.conf import settings
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets
from django.db.models import Q
import socket
from pure_pagination.mixins import PaginationMixin
from django.template.defaultfilters import slugify
from .models import AsignacionTripulacionPiloto
from .forms import AsignacionTripulacionPilotoModelForm
from infos_sistemas.mixins import TipoPerfilUsuarioMixin, AccessLoginRequiredMixin


class AsignacionTripulacionPilotoCreateView(TipoPerfilUsuarioMixin, AccessLoginRequiredMixin, CreateView):
    template_name = 'asignacion_create.html'
    form_class    = AsignacionTripulacionPilotoModelForm
    model         = AsignacionTripulacionPiloto
    success_url   = reverse_lazy('asignacion_tripulacion_piloto:create')


class AsignacionTripulacionPilotoUpdateView(TipoPerfilUsuarioMixin, AccessLoginRequiredMixin,  UpdateView):
    form_class      = AsignacionTripulacionPilotoModelForm
    success_url     = reverse_lazy('aeronave:control')
    template_name   = 'aeronave_update.html'
    queryset        = AsignacionTripulacionPiloto.objects.all()


class AsignacionTripulacionPilotoControlListView(PaginationMixin, TipoPerfilUsuarioMixin, AccessLoginRequiredMixin,  ListView):
    model         = AsignacionTripulacionPiloto
    template_name = 'asignaciones.html'
    paginate_by   = 10

    def get_context_data(self, **kwarg):
        context     = super(AsignacionTripulacionPilotoControlListView, self).get_context_data(**kwarg)
        boton_menu     = False
        total_registro = self.model.objects.count()

        data = {
            'boton_menu'    : boton_menu,
            'total_registro': total_registro,
        }

        context.update(data)
        return context

    def get(self, request, *args, **kwargs):
        if request.GET.get('search_registro', None):
            self.object_list = self.get_queryset()
            context = self.get_context_data()
            return self.render_to_response(context)
        else:
            return super(AsignacionTripulacionPilotoControlListView, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        if self.request.GET.get('search_registro', None):
            value = self.request.GET.get('search_registro', None)
            queryset = self.model.objects.filter(
            Q(slug__icontains=slugify(value))

            )
        else:
            queryset = super(AsignacionTripulacionPilotoControlListView, self).get_queryset()
        return queryset


class AsignacionTripulacionPilotoDetailView(TipoPerfilUsuarioMixin, AccessLoginRequiredMixin,  DetailView):
    template_name   = 'aeronave_detail.html'
    model           = AsignacionTripulacionPiloto
    queryset        = AsignacionTripulacionPiloto.objects.all()
