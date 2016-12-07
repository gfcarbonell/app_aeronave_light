# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from catalogos_modulos_menus_sub_menus.models import CatalogoModuloMenuSubMenu
from infos_sistemas.mixins import TipoPerfilUsuarioMixin, AccessLoginRequiredMixin

class CatalagoModuloMenuTemplateView(TipoPerfilUsuarioMixin, AccessLoginRequiredMixin, TemplateView):
	template_name = 'catologo_modulo_menu.html'

	def get_context_data(self, **kwargs):
		context = super(CatalagoModuloMenuTemplateView, self).get_context_data(**kwargs)
		boton_menu = None
		catalogos_modulos_menus = None
		if self.request.user.is_authenticated():
			catalogos_modulos_menus = CatalogoModuloMenuSubMenu.objects.filter(menu__slug='main')
		data = {
			'catalogos_modulos_menus':catalogos_modulos_menus,
			'boton_menu':boton_menu,
			}

		context.update(data)
		return context



class MantenimientoAeronaveTemplateView(TipoPerfilUsuarioMixin, AccessLoginRequiredMixin, TemplateView):
	template_name = 'mantenimiento_aeronave.html'

	def get_context_data(self, **kwargs):
		context = super(MantenimientoAeronaveTemplateView, self).get_context_data(**kwargs)
		boton_menu = None
		catalogos_modulos_menus = None
		if self.request.user.is_authenticated():
			catalogos_modulos_menus = CatalogoModuloMenuSubMenu.objects.get(modulo__slug='mantenimiento', menu__slug='main')
		data = {
			'catalogos_modulos_menus':catalogos_modulos_menus,
			'boton_menu'			 : boton_menu,
			}

		context.update(data)
		return context



class MantenimientoAeronaveMenuTemplateView(TipoPerfilUsuarioMixin, TemplateView):
	template_name = 'mantenimiento_aeronave_menu.html'

	def get_context_data(self, **kwargs):
		context = super(MantenimientoAeronaveMenuTemplateView, self).get_context_data(**kwargs)
		catalogos_modulos = None
		catalogos_modulos_menus = None
		if self.request.user.is_authenticated():
			catalogos_modulos_menus = CatalogoModuloMenuSubMenu.objects.filter(modulo__slug='mantenimiento').exclude(menu__slug ='main')
			catalogos_modulos 	    = CatalogoModuloMenuSubMenu.objects.filter(menu__slug='main')
		data = {
			'catalogos_modulos'		  : catalogos_modulos,
			'catalogos_modulos_menus' : catalogos_modulos_menus,
			}

		context.update(data)
		return context

	def get_user_id(self):
		return self.request.user.id

	def get_username(self):
		return self.request.user.username



class EmpadronamientoMunicipalMenuTemplateView(TipoPerfilUsuarioMixin, TemplateView):
	template_name = 'empadronamiento_municipal_menu.html'

	def get_context_data(self, **kwargs):
		context = super(EmpadronamientoMunicipalMenuTemplateView, self).get_context_data(**kwargs)
		catalogos_modulos = None
		catalogos_modulos_menus = None
		if self.request.user.is_authenticated():
			catalogos_modulos_menus = CatalogoModuloMenuSubMenu.objects.filter(modulo__slug='empadronamiento-municipal').exclude(menu__slug ='main')
			catalogos_modulos 	    = CatalogoModuloMenuSubMenu.objects.filter(menu__slug='main')
		data = {
			'catalogos_modulos'		  : catalogos_modulos,
			'catalogos_modulos_menus' : catalogos_modulos_menus,
			}

		context.update(data)
		return context

	def get_user_id(self):
		return self.request.user.id

	def get_username(self):
		return self.request.user.username
