from django.shortcuts import render

# Create your views here.

def index(request):
    print("El usuario entro al sistema")
    return render(request, 'core/index.html')

def onePage(request):
    return render(request, 'core/onePage.html')

def onePage(request):
    return render(request, 'core/angel.html')