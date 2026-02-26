from django import forms
from django.core.exceptions import ValidationError
import re

class RegistroForm(forms.Form):
    nombre_completo = forms.CharField(
        min_length=10,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre Completo',
            'pattern': '[A-Za-záéíóúÁÉÍÓÚñÑüÜ\s]{10,}',  # Expresión regular para nombre completo
            'title': 'Solo letras y espacios, mínimo 10 caracteres'
        })
    )

    matricula = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Matrícula UTEZ',
            'pattern': '\d{5}[A-Za-z]{2}\d{3}', 
            'title': 'Formato: 5 dígitos, 2 letras, 3 dígitos'
        })
    )

    correo = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo Institucional',
            'pattern': '[a-zA-Z0-9._%+-]+@utez\.edu\.mx',
            'title': 'Debe ser un correo válido y terminar en @utez.edu.mx'
        })
    )


    telefono = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Teléfono Móvil',
            'pattern': '\d{10}',  # Exactamente 10 dígitos
            'title': 'Exactamente 10 dígitos numéricos, sin espacios ni guiones'
        })
    )

    rfc = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'RFC',
            'pattern': '[A-Z]{4}\d{6}[A-Z0-9]{3}',  # Formato RFC: 4 letras, 6 números, 3 alfanuméricos
            'title': 'Formato: 4 letras, 6 números, 3 alfanuméricos'
        })
    )

    contraseña = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'pattern': '(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}', 
            'title': 'Mínimo 8 caracteres, al menos una mayúscula, una minúscula, un número y un símbolo especial (@$!%*?&)'
        })
    )


    
    def clean_matricula(self):
        matricula = self.cleaned_data['matricula']
        if not re.match(r'^\d{5}[A-Za-z]{2}\d{3}$', matricula):
            raise ValidationError('La matrícula debe tener el formato: 5 dígitos, 2 letras, 3 dígitos.')
        return matricula

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if not re.match(r'^\d{10}$', telefono):
            raise ValidationError('El teléfono debe tener exactamente 10 dígitos numéricos, sin espacios ni guiones.')
        return telefono

    def clean_rfc(self):
        rfc = self.cleaned_data['rfc']
        if not re.match(r'^[A-Z]{4}\d{6}[A-Z0-9]{3}$', rfc):
            raise ValidationError('El RFC debe tener el formato: 4 letras, 6 números, 3 alfanuméricos.')
        return rfc

    def clean_contraseña(self):
        contraseña = self.cleaned_data['contraseña']
        if not re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$', contraseña):
            raise ValidationError('La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula, un número y un símbolo especial.')
        return contraseña
    
    def clean_correo(self):
        correo = self.cleaned_data['correo']
        if not correo.endswith('@utez.edu.mx'):
            raise ValidationError('El correo debe terminar con @utez.edu.mx')
        return correo

