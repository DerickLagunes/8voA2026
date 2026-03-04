from rest_framework import viewsets
from .models import Libro   # <-- El modelo
from .serializers import LibroSerializer  # <-- El serializador


class LibroViewSet(viewsets.ModelViewSet):

    queryset = Libro.objects.all()
    serializer_class = LibroSerializer