# -*- encoding: utf-8 -*-
from django.conf import settings
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets
from django.db.models import Q
import socket
from pure_pagination.mixins import PaginationMixin
from django.template.defaultfilters import slugify
from .models import CatalogoAeronaveParteAveria
from infos_sistemas.mixins import TipoPerfilUsuarioMixin, AccessLoginRequiredMixin


class CatalogoAeronaveParteAveriaControlListView(PaginationMixin, TipoPerfilUsuarioMixin, AccessLoginRequiredMixin,  ListView):
    model         = CatalogoAeronaveParteAveria
    template_name = 'aeronaves.html'
    paginate_by   = 10

    def get_context_data(self, **kwarg):
        context     = super(CatalogoAeronaveParteAveriaControlListView, self).get_context_data(**kwarg)
        boton_menu     = False
        total_registro = self.model.objects.count()

        data = {
            'boton_menu'    : boton_menu,
            'total_registro': total_registro,
        }

        context.update(data)
        return context

    def get(self, request, *args, **kwargs):
        if request.GET.get('search_aeronave', None):
            self.object_list = self.get_queryset()
            context = self.get_context_data()
            return self.render_to_response(context)
        else:
            return super(CatalogoAeronaveParteAveriaControlListView, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        if self.request.GET.get('search_aeronave', None):
            value = self.request.GET.get('search_aeronave', None)
            queryset = self.model.objects.filter(
           		Q(catalogo_aeronave_parte__aeronave=value)
            )
        else:
            queryset = super(CatalogoAeronaveParteAveriaControlListView, self).get_queryset()
        return queryset
