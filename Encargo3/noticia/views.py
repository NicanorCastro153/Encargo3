from django.shortcuts import render

# Create your views here.

# opciones navbar
def home(request):
    return render(request, 'menu/home.html')

def actualidad(request):
    return render(request, 'menu/actualidad.html')

def contactanos(request):
    return render(request, 'menu/contactanos.html')

def deporte(request):
    return render(request, 'menu/deporte.html')

def economia(request):
    return render(request, 'menu/economia.html')

# noticias
def noticiaArsenal(request):
    return render(request, 'noticias/noticiaArsenal.html')

def noticiaBasketball(request):
    return render(request, 'noticias/noticiaBasketball.html')

def noticiaEconomia(request):
    return render(request, 'noticias/noticiaEconomia.html')

def noticiaEncerrona(request):
    return render(request, 'noticias/noticiaEncerrona.html')

def noticiaMonroe(request):
    return render(request, 'noticias/noticiaMonroe.html')

def noticiaNintendo(request):
    return render(request, 'noticias/noticiaNintendo.html')

def noticiaTenis(request):
    return render(request, 'noticias/noticiaTenis.html')

def noticiaLula(request):
    return render(request, 'noticias/noticiaLula.html')

def noticiaeli(request):
    return render(request, 'noticias/noticiaEli.html')

