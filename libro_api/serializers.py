from rest_framework import serializers
from .models import Libro  # <-- modelo a serializar


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = "__all__"  # expone todos los campos (id, titulo, autor, isbn, etc.)