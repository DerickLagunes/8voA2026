from django.urls import path

from core import views as core

urlpatterns = [
    path('',core.index,name='index'),
    path('onePage/', core.onePage, name='onePage'),
    path('derick/', core.derick, name='derick'),
    path('cristian/', core.cristian, name='cristian')
]
