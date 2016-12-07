# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.template.defaultfilters import slugify

from personas.models import Persona
from cargos.models import Cargo
from tipos_pilotos.models import TipoPiloto
from areas.models import Area


class Piloto(Persona):
    BOOL_ACTIVO 		 			= ((True, 'Si'), (False, 'No'))
    tipo_piloto                     = models.ForeignKey(TipoPiloto)
    apelativo                       = models.CharField(max_length=255)
    area		                    = models.ForeignKey(Area)
    cargo 	  	                    = models.ForeignKey(Cargo,verbose_name="Cargo - Grado" )
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
        super(Piloto, self).save(*args, **kwargs)

    #Opciones
    class Meta:
        #Nombre para la tabla del gestor de base de datos
        db_table = 'Pilotos'
        #Ordenar los registros por un campo especifico
        ordering = ('apellido_paterno',)
        #Nombre para el Conjunto de Objetos en el Panel de Administración
        verbose_name = 'Piloto'
        #Nombre en Plural en la lista de módulos en el Panel de Administración
        verbose_name_plural = 'Pilotos'#Métodos
