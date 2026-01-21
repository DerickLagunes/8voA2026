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

