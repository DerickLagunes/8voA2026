from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Libro
from .forms import LibroForm
import json


# 1. LISTAR (GET)
def get_libros(request):
    libros = Libro.objects.all().values()
    return JsonResponse(list(libros), safe=False)

# 2. CREAR (POST)
@csrf_exempt
def create_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'mensaje': 'Libro creado correctamente'
            }, status=201)
        else:
            return JsonResponse({
                'mensaje': 'Error de registro',
                'errores': form.errors
            }, status=422)

    return JsonResponse({'error': 'Método no permitido'}, status=405)

# 3. ACTUALIZAR (PUT/POST)
@csrf_exempt
def update_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)

        form = LibroForm(data, instance=libro)

        if form.is_valid():
            form.save()
            return JsonResponse({
                'mensaje': 'Libro actualizado correctamente'
            }, status=200)

        else:
            return JsonResponse({
                'errores': form.errors
            }, status=422)

    return JsonResponse({'error': 'Método no permitido'}, status=405)

# 4. ELIMINAR (DELETE)
@csrf_exempt
def delete_libro(request, pk):
    if request.method == 'DELETE':
        libro = get_object_or_404(Libro, pk=pk)
        libro.delete()
        return JsonResponse({'mensaje': 'Libro eliminado'}, status=204)
    return JsonResponse({'error': 'Método no permitido'}, status=405)