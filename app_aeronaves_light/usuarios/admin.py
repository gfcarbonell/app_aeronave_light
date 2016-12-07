# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario
from .forms import UsuarioModelForm


@admin.register(Usuario)
# Por defecto el admin usa -> UserAdmin
class UsuarioAdmin(UserAdmin):

	list_display = ('username', 'email', 'password',)

	search_fields  = ('username', 'id')

	fieldsets = (
			('Usuario', {'fields':('username', 'password', 'email',)}),

			('Permissions', {'fields':('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
		)
	class Meta:
		model = Usuario
