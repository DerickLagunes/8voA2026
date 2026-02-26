from django.shortcuts import render
from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # datos en consola
            print("Formulario válido. Datos del registro:")
            print("Nombre Completo:", form.cleaned_data['nombre_completo'])
            print("Matrícula:", form.cleaned_data['matricula'])
            print("Correo:", form.cleaned_data['correo'])
            print("Teléfono:", form.cleaned_data['telefono'])
            print("RFC:", form.cleaned_data['rfc'])
            print("Contraseña:", form.cleaned_data['contraseña']) 

            
            return render(request, 'registro/datosRegistro.html', {'datos': form.cleaned_data})
        else:
            #errores en la consola
            print("Formulario no válido. Errores:")
            for field in form:
                for error in field.errors:
                    print(f"Error en el campo '{field.label}': {error}")
            
            return render(request, 'registro/registro.html', {'form': form, 'mensaje': 'Hubo errores en el formulario, verifica los datos ingresados.'})
    else:
        form = RegistroForm()

    return render(request, 'registro/registro.html', {'form': form})

def datosRegistro(request):
    return render(request, 'registro/datosRegistro.html')