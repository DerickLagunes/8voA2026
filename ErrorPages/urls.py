from django.urls import path

from core import views as core

urlpatterns = [
    path('',core.index,name='index'),
    path('onePage/', core.onePage, name='onePage'),
    path('derick/', core.derick, name='derick'),
    path('astrid/', core.astrid, name='astrid'),
    path('cristian/', core.cristian, name='cristian'),
    path('viri/', core.viri, name='viri'),
    path('orlando/', core.orlando, name='orlando'),
    path('johanna/', core.johanna,name='johanna'),
    path('ander/', core.ander, name='ander'),
    
    path('rocio/', core.rocio, name='rocio'),

    path('sebas/', core.sebas, name='sebas')    
]
