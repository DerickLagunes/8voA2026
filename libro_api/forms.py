from django import forms
from .models import Libro
from django.core.exceptions import ValidationError
import re


class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'isbn', 'paginas', 'editorial', 'disponible']

        labels = {
            'titulo': 'Título del libro',
            'autor': 'Autor del libro',
            'isbn': 'ISBN del libro',
            'paginas': 'Número de páginas',
            'editorial': 'Editorial del libro',
            'disponible': '¿Está disponible?',
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej. Cien años de soledad'}),
            'autor': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej. Gabriel García Márquez'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej. 9780140283334'}),
            'paginas': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Ej. 400','min': '1'}),
            'editorial': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej. Editorial Sudamericana'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    #validar la información que me va a llegar en los campos

    def clean_titulo(self):
        data = self.cleaned_data['titulo']

        if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9\s\.,\-]+$', data):
            raise ValidationError("El título solo puede contener letras, números, espacios y signos básicos.")

        if len(data.strip()) < 2:
            raise ValidationError("El título es demasiado corto.")

        return data.strip()

    def clean_autor(self):
        data = self.cleaned_data['autor']

        if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s\.]+$', data):
            raise ValidationError("El autor solo puede contener letras y espacios.")

        return data.strip()

    def clean_isbn(self):
        data = self.cleaned_data['isbn']

        # Quitar guiones para validar longitud real
        isbn_limpio = data.replace("-", "")

        if not isbn_limpio.isdigit():
            raise ValidationError("El ISBN solo debe contener números (puede incluir guiones).")

        if len(isbn_limpio) not in [10, 13]:
            raise ValidationError("El ISBN debe tener 10 o 13 dígitos.")

        return data

    def clean_paginas(self):
        data = self.cleaned_data['paginas']

        if data <= 0:
            raise ValidationError("El número de páginas debe ser mayor a 0.")

        if data > 5000:
            raise ValidationError("Número de páginas poco realista.")

        return data

    def clean_editorial(self):
        data = self.cleaned_data['editorial']

        if len(data.strip()) < 2:
            raise ValidationError("La editorial es demasiado corta.")

        return data.strip()