# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from infos_sistemas.models import InfoSistema
from django.template.defaultfilters import slugify

from personas.models import Persona
from cargos.models import Cargo
from tipos_empleados.models import TipoEmpleado
from usuarios.models import Usuario
from areas.models import Area


class Empleado(Persona):
	BOOL_ACTIVO 		 			= ((True, 'Si'), (False, 'No'))
	area							= models.ForeignKey(Area)
	usuario							= models.OneToOneField(Usuario, unique=True, related_name='usuario_empleados_related')
	tipo_empleado    				= models.ForeignKey(TipoEmpleado, verbose_name="Tipo especialista" )
	cargo 	  				    	= models.ForeignKey(Cargo,verbose_name="Cargo - Grado" )
	activo 							= models.BooleanField(choices=BOOL_ACTIVO, default=True)

	#Métodos
	#Python 3.X
	def __str__(self):
		return self.get_nombre_completo()

	#Python 2.X
	#def __unicode__(self):
	#	return self.nombre

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_nombre_completo())
		else:
			slug = slugify(self.get_nombre_completo())
			if self.slug != slug:
				self.slug = slug
		super(Empleado, self).save(*args, **kwargs)

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos
		db_table = 'Empleados'
		#Ordenar los registros por un campo especifico
		ordering = ('apellido_paterno',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Empleado'
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Empleados'#Métodos
