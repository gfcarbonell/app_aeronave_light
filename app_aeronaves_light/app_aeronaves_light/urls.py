from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from usuarios.views import UsuarioViewSet, PermissionViewSet, GroupViewSet, ContentTypeViewSet
from documentos_identificaciones.views import DocumentoIdentificacionViewSet
router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'content_type', ContentTypeViewSet)
router.register(r'documentos_identificaciones', DocumentoIdentificacionViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',                           include('catalogos_modulos_menus_sub_menus.urls', namespace='catalogo_modulo_menu_sub_menu')),
    url(r'^mantenimiento/', 	        include('aeronaves.urls', namespace='aeronave')),
    url(r'^mantenimiento/', 	        include('pilotos.urls', namespace='piloto')),
    url(r'^mantenimiento/', 	        include('empleados.urls', namespace='empleado')),
    url(r'^mantenimiento/',             include('asignaciones_tripulaciones_pilotos.urls', namespace='asignacion_tripulacion_piloto')),
    url(r'^mantenimiento/',             include('ordenes_vuelos.urls', namespace='orden_vuelo')),
    url(r'^mantenimiento/', 	        include('catalogos_aeronaves_partes_averias_soluciones_empleados.urls', namespace='catalogo_aeronave_parte_averia_solucion_empleado')),
    url(r'^mantenimiento/',             include('catalogos_aeronaves_partes_averias.urls', namespace='catalogo_aeronave_parte_averia')),

    url(r'^', 	                        include('usuarios.urls', namespace='usuario')),
  	
    #REST
    url(r'^api/', 						include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
