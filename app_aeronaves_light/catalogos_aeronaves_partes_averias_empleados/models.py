# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from empleados.models import Empleado
from catalogos_aeronaves_partes_averias.models import CatalogoAeronaveParteAveria
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify


class CatalogoAeronaveParteAveriaEmpleado(models.Model):
    BOOL_ACTIVO 		 			             = ((True, 'Si'), (False, 'No'))
    catalogos_aeronaves_partes_averias = models.ForeignKey(CatalogoAeronaveParteAveria)
    empleado                           = models.ForeignKey(Empleado)

    descripcion		    			           = models.TextField(verbose_name='Observación', blank=True, null=True, help_text='(Opcional)')
    observacion		   				           = models.TextField(verbose_name='Descripción', blank=True, null=True, help_text='(Opcional)')
    seleccionar 					             = models.BooleanField(default=True, choices=BOOL_ACTIVO)
    slug                               = models.SlugField(editable=False, max_length=255 ,unique=True, db_index=True, )

    #Métodos
    #Python 3.X
    def __str__(self):
      return self.get_nombre()

    #Python 2.X
    #def __unicode__(self):
    #	return self.nombre

    def save(self, *args, **kwargs):
      if not self.pk:
        self.slug = slugify(self.get_nombre())
      else:
        slug = slugify(self.get_nombre())
        if self.slug != slug:
          self.slug = slug
      super(CatalogoAeronaveParteAveriaEmpleado, self).save(*args, **kwargs)

    def get_nombre(self):
      return ' %s | %s ' %(self.catalogos_aeronaves_partes_averias.get_nombre() , self.averia.get_nombre())

    #Opciones
    class Meta:
      #Nombre para la tabla del gestor de base de datos
      db_table = 'Catalogos_Aeronaves_Partes_Averias_Empleado'
      #Ordenar los registros por un campo especifico
      #ordering = ('orden_aeronave','orden_parte_aeronave', )
      #Nombre para el Conjunto de Objetos en el Panel de Administración
      verbose_name = 'Catalogo Aeronave Parte Averias Empleado'
      #Nombre en Plural en la lista de módulos en el Panel de Administración
      verbose_name_plural = 'Catalogos Aeronaves Partes Averias Empleado'
