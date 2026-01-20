from django.shortcuts import render

def index(request):
    #Codigo backend
    return render(request, 'core/index.html')

def onePage(request):
    return render(request, 'core/onePage.html')

def juan(request):
    return render(request, 'core/juan.html')