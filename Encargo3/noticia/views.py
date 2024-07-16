from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from .models import Asunto, MensajeUsuario, Noticia, TipoNoticia
from .forms import AsuntoForm, MensajeUsuarioForm, NoticiaForm, TipoNoticiaForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

# Create your views here.

# opciones navbar
def home(request):
    context={}
    return render(request, 'menu/home.html',context)

def actualidad(request):
    context={}
    return render(request, 'menu/actualidad.html',context)

def contactanos(request):
    context={}
    return render(request, 'menu/contactanos.html',context)

def deporte(request):
    context={}
    return render(request, 'menu/deporte.html',context)

def economia(request):
    context={}
    return render(request, 'menu/economia.html',context)

def Iniciar_sesion(request):
    context={}
    return render(request, 'menu/Iniciar_sesion.html',context)


# noticias
def noticiaArsenal(request):
    context={}
    return render(request, 'noticias/noticiaArsenal.html',context)

def noticiaBasketball(request):
    context={}
    return render(request, 'noticias/noticiaBasketball.html',context)

def noticiaEconomia(request):
    context={}
    return render(request, 'noticias/noticiaEconomia.html',context)

def noticiaEncerrona(request):
    context={}
    return render(request, 'noticias/noticiaEncerrona.html',context)

def noticiaMonroe(request):
    context={}
    return render(request, 'noticias/noticiaMonroe.html',context)

def noticiaNintendo(request):
    context={}
    return render(request, 'noticias/noticiaNintendo.html',context)

def noticiaTenis(request):
    context={}
    return render(request, 'noticias/noticiaTenis.html',context)

def noticiaLula(request):
    context={}
    return render(request, 'noticias/noticiaLula.html',context)

def noticiaeli(request):
    context={}
    return render(request, 'noticias/noticiaEli.html',context)

#forms
def AgregarNoticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('AgregarNoticia.html')
    else:
        form = NoticiaForm()

    return render(request, 'forms/AgregarNoticia.html', {'form': form})
#forms
def AgregarTipoNoticia(request):
    if request.method == 'POST':
        form = TipoNoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('AgregarTipoNoticia.html')
    else:
        form = TipoNoticiaForm()

    return render(request, 'forms/AgregarTipoNoticia.html', {'form': form})
#forms
def AgregarAsunto(request):
    if request.method == 'POST':
        form = AsuntoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('AgregarAsunto')
    else:
        form = AsuntoForm()

    return render(request, 'forms/AgregarAsunto.html', {'form': form})
#forms
def Contactanos(request):
    if request.method == 'POST':
        form = MensajeUsuarioForm(request.POST) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('Contactanos.html')
    else:
        form = MensajeUsuarioForm()

    return render(request, 'forms/Contactanos.html', {'form': form})

def contactanos(request):
    if request.method == "GET":
        asuntos = Asunto.objects.all()
        context = {'asuntos': asuntos}
        return render(request, 'menu/contactanos.html', context)
    else:
        nombre = request.POST.get("nombre")
        correo = request.POST.get("correo")
        asunto_id = request.POST.get("asunto")
        motivo = request.POST.get("motivo")

        asunto = Asunto.objects.get(id_asunto=asunto_id)
        mensaje = MensajeUsuario.objects.create(
            nombre=nombre,
            correo=correo,
            asunto=asunto,
            motivo=motivo,
        )
        mensaje.save()

        asuntos = Asunto.objects.all()
        context = {
            'asuntos': asuntos,
            'mensaje': '¡Mensaje enviado correctamente!',
            'alerta_tipo': 'success'
        }
        return render(request, 'menu/contactanos.html', context)



def registrar(request):
    if request.method == 'GET':
        return render(request, "menu/registrar.html", {'form': UserCreationForm})
    else:
        if request.POST["password1"] != request.POST["password2"]:
            return render(request, 'menu/registrar.html', {'form': UserCreationForm, 'Error': "Las contraseñas no coinciden"})
        else:
            email = request.POST.get("email")
            name = request.POST.get("username")
            if User.objects.filter(email=email).exists():
                return render(request, 'menu/registrar.html', {'form': UserCreationForm, 'Error': "El correo ya está registrado"})
            elif User.objects.filter(username=name).exists():
                return render(request, 'menu/registrar.html', {'form': UserCreationForm, 'Error': "Usuario ya existente"})
            else:
                password = request.POST["password1"]
                user = User.objects.create_user(username=name, password=password, email=email)
                user.save()
                return render(request, 'menu/registrar.html', {'form': UserCreationForm, 'Success': "Usuario Registrado"})
            
            
def Iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'menu/Iniciar_sesion.html', {'form': AuthenticationForm()})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'menu/Iniciar_sesion.html', {'form': AuthenticationForm(), 'Error': 'Usuario y/o Contraseña Incorrecta'})
        else:
            login(request, user)
            if user.is_superuser:
                return redirect('PanelAdministrador')
            else:
                return redirect('home')
            
def logout_view(request):
    logout(request)
    return redirect('home')
      
        
@login_required
@user_passes_test(lambda u: u.is_superuser)
def PanelAdministrador(request):
    mensajes = MensajeUsuario.objects.all()
    noticias = Noticia.objects.all()
    tipos = TipoNoticia.objects.all()
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        tipo_id = request.POST['tipo']
        imagen = request.FILES['imagen']
        tipo_noticia = TipoNoticia.objects.get(pk=tipo_id)
        nueva_noticia = Noticia(
            titulo=titulo,
            descripcion=descripcion,
            tipo=tipo_noticia,
            imagen=imagen
        )
        nueva_noticia.save()
        return redirect('PanelAdministrador')
    context = {
        'noticias': noticias,
        'mensajes': mensajes,
        'tipos': tipos
    }
    return render(request, 'admin/PanelAdministrador.html', context)

def noticia_del(request, pk):
    context = {}
    try:
        noticia = get_object_or_404(Noticia, id_noticia=pk)
        noticia.delete()
        noticias = Noticia.objects.all()
        context = {'noticias': noticias
                   }
        redirect('menu/home')
    except Noticia.DoesNotExist:

        noticias = Noticia.objects.all()
        context = {'noticias': noticias
                   }
    return render(request, 'admin/PanelAdministrador.html', context)


def ultimas_noticias(request):
    noticias = Noticia.objects.all()
    context = {'noticias': noticias}
    return render(request, 'menu/ultimas_noticias.html',context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def buscar_noticia(request, pk):
    if pk!="":
       noticia=Noticia.objects.get(id_noticia=pk)
       tipos = TipoNoticia.objects.all()
       id_tipo_ = noticia.tipo.tipo  
       context={
           "noticia":noticia,
            "tipos": tipos, 
            "id_tipo_": id_tipo_
            }
    if noticia:
        return render(request, 'admin/buscar_noticia.html', context)
    else:
        context={"mensaje": "Error, no existe el rut..."}
        return render(request, 'admin/buscar_noticia.html', context)
    

def modificar_noticia(request, pk):
    noticia = Noticia.objects.get(id_noticia=pk)
    tipos = TipoNoticia.objects.all()

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        tipo_id = request.POST.get('tipo')
        imagen = request.FILES.get('imagen')
        noticia.titulo = titulo
        noticia.descripcion = descripcion
        noticia.tipo_id = tipo_id
        if imagen:
            noticia.imagen = imagen
        noticia.save()
        return redirect('PanelAdministrador')
    context = {
        'noticia': noticia,
        'tipos': tipos,
    }
    return render(request, 'admin/buscar_noticia.html', context)    