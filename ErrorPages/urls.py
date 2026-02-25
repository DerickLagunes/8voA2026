from django.urls import path
from core import views as core
from mascota_api import views as mascota_api

urlpatterns = [
    path('', core.index, name='index'),
    path('onePage/', core.onePage, name='onePage'),
    path('juan/', core.juan, name='juan'),
    path('derick/', core.derick, name='derick'),
    path('cesar/', core.cesar, name='cesar'),
    path('astrid/', core.astrid, name='astrid'),
    path('cristian/', core.cristian, name='cristian'),
    path('viri/', core.viri, name='viri'),
    path('orlando/', core.orlando, name='orlando'),
    path('johanna/', core.johanna,name='johanna'),
    path('buscar/', core.buscador, name="busqueda"),
    path('api/buscar/', core.buscar_en_google, name='api_buscar'),
    path('contacto/', core.contacto_view, name='contacto'),

    path('operacion/', core.operacion, name='operacion'),
    
    path('get/contacto/',core.getall_contacto,name='getall_contacto'),
    path('create/contacto/',core.create_contacto, name='create_contacto'),

    path('obtener/mascotas/',mascota_api.get_mascotas,name='obtener_mascotas'),
    path('nueva/mascota/',mascota_api.create_mascota,name='x'),
    path('editar/mascota/<int:pk>/',mascota_api.update_mascota,name='y'),
    path('borrar/mascota/<int:pk>/',mascota_api.delete_mascota,name='z'),


]
