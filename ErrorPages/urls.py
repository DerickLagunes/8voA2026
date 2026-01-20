from django.urls import path
from core import views as core

urlpatterns = [
    path('', core.index, name='index'),
    path('onePage/', core.onePage, name='onePage'),
    path('juan/', core.juan, name='juan'),
]