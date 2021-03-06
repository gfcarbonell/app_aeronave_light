# -*- encoding: utf-8 -*-
from django.conf import settings
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from .models import Piloto
from .forms import PilotoModelForm
from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets
from django.db.models import Q
import socket
from pure_pagination.mixins import PaginationMixin
from django.template.defaultfilters import slugify

from infos_sistemas.mixins import TipoPerfilUsuarioMixin, AccessLoginRequiredMixin


class PilotoCreateView(TipoPerfilUsuarioMixin, AccessLoginRequiredMixin, CreateView):
    form_class      = PilotoModelForm
    success_url     = reverse_lazy('piloto:control')
    template_name   = 'piloto_create.html'


class PilotoUpdateView(TipoPerfilUsuarioMixin, AccessLoginRequiredMixin, UpdateView):
    form_class      = PilotoModelForm
    success_url     = reverse_lazy('piloto:control')
    template_name   = 'piloto_update.html'
    queryset        = Piloto.objects.all()

    def get_context_data(self, **kwarg):
        context  = super(PilotoUpdateView, self).get_context_data(**kwarg)
        empleado  = self.queryset.get(slug__contains=self.kwargs['slug'])
        data = {'empleado':empleado}
        context.update(data)
        return context


class PilotoControlListView(PaginationMixin, TipoPerfilUsuarioMixin, AccessLoginRequiredMixin, ListView):
    model         = Piloto
    template_name = 'pilotos.html'
    paginate_by   = 10

    def get_context_data(self, **kwarg):
        context     = super(PilotoControlListView, self).get_context_data(**kwarg)
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
            return super(PilotoControlListView, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        if self.request.GET.get('search_registro', None):
            value = self.request.GET.get('search_registro', None)
            queryset = self.model.objects.filter(Q(slug__icontains=slugify(value)))
        else:
            queryset = super(PilotoControlListView, self).get_queryset()
        return queryset


class PilotoDetailView(TipoPerfilUsuarioMixin, AccessLoginRequiredMixin, DetailView):
    template_name   = 'piloto_detail.html'
    model           = Piloto
    queryset        = Piloto.objects.all()
