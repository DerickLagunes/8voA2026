from django.shortcuts import render

def index(request):
    #Codigo backend
    return render(request, 'core/index.html')

def onePage(request):
    return render(request, 'core/onePage.html')

def juan(request):
    return render(request, 'core/juan.html')

def derick(request):
    print("")
    return render(request, 'core/derick.html')

def astrid(request):
    return render(request, 'core/astrid.html')

def cristian (request):
    return render(request, 'core/Cristian.html')

def cesar(request):
    return render(request, 'core/cesar.html')

def viri(request):
    return render(request, 'core/viri.html')

def orlando(request):
    return render(request, 'core/orlando.html')

def johanna(request):
    print("Soy Johanna")
    return render(request, "core/johanna.html")

def buscador(request):
    return render(request, 'core/busqueda.html')


import requests
from django.conf import settings
from django.http import JsonResponse

def buscar_en_google(request):
    query = request.GET.get('q', '')
    if not query:
        return JsonResponse({'error': 'No se proporcionó búsqueda'}, status=400)

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': settings.GOOGLE_SEARCH_API_KEY,
        'cx': settings.GOOGLE_SEARCH_CX,
        'q': query
    }

    response = requests.get(url, params=params)
    return JsonResponse(response.json())


from django.shortcuts import render
from .forms import ContactoForm
from core.models import Contacto
from django.http import JsonResponse

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Los datos ya pasaron las validaciones de front y back
            form.save()
            return JsonResponse({
                'status':'ok',
                'mensaje':'Registro exitoso!',
            })
        else:
            return JsonResponse({
                'status':'error',
                'mensaje': 'Algo salio mal',
                'errors': form.errors
            })
    else:
        form = ContactoForm()
    return render(
        request, 
        'core/contacto.html', 
        {
            'form': form, 
            'contactos': Contacto.objects.all()
        }
    )

# Operación que no es de CRUD
def operacion(request):
    if request.method == 'POST': #Quiere hacer suma
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        resultado = int(num1) + int(num2)
        return JsonResponse({'respuesta':resultado})
    elif request.method == 'GET': # Resta
        num1 = request.GET('num1')
        num2 = request.GET('num2')
        resultado = int(num1) - int(num2)
        return JsonResponse({'respuesta':resultado})
    else:
       return JsonResponse({'respuesta':'No puedes usar otro metodo que no sea GET o POST'}) 



## Operaciones CRUD (requiere un modelo)
#  con API REST (artesanal)

# from core.models import Contacto
# from core.forms import contacto_form
# GET (Get all)
def getall_contacto(request):
    datos = Contacto.objects.values()
    datos_formateados = list(datos)
    return JsonResponse(datos_formateados, safe=False)

# POST (create)
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_contacto(request): # <----Me esta llegando info de un form
    nombre = request.POST['nombre']
    email = request.POST['email']
    mensaje = request.POST['mensaje']
    Contacto.objects.create( # Esto no activa los clean del form
        nombre = nombre,
        email = email,
        mensaje = mensaje
    )
    return JsonResponse({'mensaje': 'registro exitoso'})


        


