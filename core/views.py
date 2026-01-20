from django.shortcuts import render

def index(request):
    #Código backend
    return render(request, 'core/index.html')

def onePage(request):
    return render(request, 'core/onePage.html')

def derick(request):
    print("")
    return render(request, 'core/derick.html')

def cristian (request):
    return render(request, 'core/Cristian.html')

def viri(request):
    return render(request, 'core/viri.html')