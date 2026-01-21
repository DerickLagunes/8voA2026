from django.shortcuts import render

def index(request):
    #Código backend
    return render(request, 'core/index.html')

def onePage(request):
    return render(request, 'core/onePage.html')

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
def erick(request):
    return render(request, 'core/erick.html')

def ander(request):
    print("Soy Ander")
    return render(request, "core/ander.html")
def sebas(request):
    return render(request, "core/sebas.html")

def elias(request):
    return render(request, "core/elias.html")
def rocio(request):
    return render(request, 'core/rocio.html')

def alexa(request):
    return render(request, 'core/alexa.html')
def emiliano(request):
    return render(request, 'core/emiliano.html')
