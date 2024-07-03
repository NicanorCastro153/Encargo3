from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Asunto, MensajeUsuario, Noticia, TipoNoticia
from .forms import AsuntoForm, MensajeUsuarioForm, NoticiaForm, TipoNoticiaForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
0
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

def Iniciar_sesion(request):
    return render(request, 'menu/Iniciar_sesion.html')

def registrar(request):
    return render(request, 'menu/registrar.html')

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




def AgregarNoticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)  # Asegúrate de incluir request.FILES para manejar archivos
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('AgregarNoticia.html')
    else:
        form = NoticiaForm()

    return render(request, 'admin/AgregarNoticia.html', {'form': form})

def AgregarTipoNoticia(request):
    if request.method == 'POST':
        form = TipoNoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('AgregarTipoNoticia.html')
    else:
        form = TipoNoticiaForm()

    return render(request, 'admin/AgregarTipoNoticia.html', {'form': form})

def AgregarAsunto(request):
    if request.method == 'POST':
        form = AsuntoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('AgregarAsunto')
    else:
        form = AsuntoForm()

    return render(request, 'admin/AgregarAsunto.html', {'form': form})

def Contactanos(request):
    if request.method == 'POST':
        form = MensajeUsuarioForm(request.POST) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('Contactanos.html')
    else:
        form = MensajeUsuarioForm()

    return render(request, 'Contactanos.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige al home después de iniciar sesión
        else:
            messages.error(request, 'Credenciales incorrectas.')
    return render(request, 'Iniciar_sesion.html')



