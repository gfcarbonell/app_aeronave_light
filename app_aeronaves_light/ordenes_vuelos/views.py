# -*- encoding: utf-8 -*-
from django.conf import settings
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets
from django.db.models import Q
import socket
from pure_pagination.mixins import PaginationMixin
from django.template.defaultfilters import slugify
from .models import OrdenVuelo
from .forms import OrdenVueloModelForm
from infos_sistemas.mixins import TipoPerfilUsuarioMixin, AccessLoginRequiredMixin


class OrdenVueloCreateView(TipoPerfilUsuarioMixin, AccessLoginRequiredMixin, CreateView):
    template_name = 'orden_vuelo_create.html'
    form_class    = OrdenVueloModelForm
    model         = OrdenVuelo
    success_url   = reverse_lazy('orden_vuelo:control')


class OrdenVueloUpdateView(TipoPerfilUsuarioMixin, AccessLoginRequiredMixin,  UpdateView):
    form_class      = OrdenVueloModelForm
    success_url     = reverse_lazy('orden_vuelo:control')
    template_name   = 'orden_vuelo_update.html'
    queryset        = OrdenVuelo.objects.all()


class OrdenVueloControlListView(PaginationMixin, TipoPerfilUsuarioMixin, AccessLoginRequiredMixin,  ListView):
    model         = OrdenVuelo
    template_name = 'ordenes_vuelos.html'
    paginate_by   = 10

    def get_context_data(self, **kwarg):
        context     = super(OrdenVueloControlListView, self).get_context_data(**kwarg)
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
            return super(OrdenVueloControlListView, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        if self.request.GET.get('search_registro', None):
            value = self.request.GET.get('search_registro', None)
            queryset = self.model.objects.filter(
            Q(slug__icontains=slugify(value))

            )
        else:
            queryset = super(OrdenVueloControlListView, self).get_queryset()
        return queryset


class OrdenVueloDetailView(TipoPerfilUsuarioMixin, AccessLoginRequiredMixin,  DetailView):
    template_name   = 'orden_vuelo_detail.html'
    model           = OrdenVuelo
    queryset        = OrdenVuelo.objects.all()
