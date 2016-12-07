# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from django.core.validators import validate_ipv46_address
from django.template.defaultfilters import slugify
import socket
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.core.validators import EmailValidator
import os
from django.conf import settings



class UserManager(BaseUserManager):
	def _create_user(self, username, email, password, **extra_fields):
		if not username:
			raise ValueError('the given username must be set')
		email = self.normalize_email(email)
		user = self.model(username = username, email = email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, username, email=None, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(username, email, password, **extra_fields)

	def create_superuser(self, username, email, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')
		return self._create_user(username, email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
	username 						= models.CharField(
														verbose_name='Nombre de usuario',
														max_length=50,
														unique=True,
														db_index=True,
														validators=[
															        MinLengthValidator(2),
															        MaxLengthValidator(50),
															    ]
													  )
	email    						= models.EmailField(
														max_length=100,
														unique=True,
														db_index=True,
														validators=[
															EmailValidator(),
														]
													   )
	slug							= models.SlugField(editable=False, max_length=255 ,unique=True, db_index=True, )
	
	objects = UserManager()

	is_active = models.BooleanField(default=True)
	is_staff  = models.BooleanField(default=True)

	USERNAME_FIELD  = 'username'
	REQUIRED_FIELDS = ['email',]

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.username)
		else:
			slug = slugify(self.username)
			if self.slug != slug:
				self.slug = slug
		super(Usuario, self).save(*args, **kwargs)

	def get_short_name(self):
		return self.username

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos
		db_table = 'Usuarios'
		#Ordenar los registros por un campo especifico
		ordering = ('username',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Usuario'
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Usuarios'
