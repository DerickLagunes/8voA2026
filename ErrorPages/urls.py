from django.urls import path
from core import views as core
from registro import views as registro

urlpatterns = [
    path('',core.index,name='index'),
    path('onePage/', core.onePage, name='onePage'),
    path('derick/', core.derick, name='derick'),
    path('astrid/', core.astrid, name='astrid'),
    path('cristian/', core.cristian, name='cristian'),
    path('viri/', core.viri, name='viri'),
    path('orlando/', core.orlando, name='orlando'),
    path('registro/', registro.registro, name='registro'),
    path('datosRegistro/', registro.datosRegistro, name='datosRegistro'),
]
