from django.urls import path

from core import views as core

urlpatterns = [
    path('', core.index,name='index'),
    path('nuevo', core.index,name='nuevo'),
    path('onePage/', core.onePage, name='onePage'),
    path('angel/', core.onePage, name='angel'),
    
]
