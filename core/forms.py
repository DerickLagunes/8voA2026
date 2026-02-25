from django import forms
from django.core.exceptions import ValidationError
from core.models import Contacto
import re

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre','apellidos','email','mensaje']

    # Validación de Backend
    def clean_nombre(self):
        data = self.cleaned_data['nombre']
        if not re.match('^[a-zA-ZáéúíóÁÉÚÍÓ]{3,}$', data):
            raise ValidationError("Oye no puedes ingresar numeros, solo letras")
        return data

    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if "spam" in data.lower():
            raise ValidationError("No se permite contenido publicitario.")
        return data
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if "@utez.edu.mx" not in data:
            raise ValidationError("Solo puedes registrar correos de la utez")
        return data