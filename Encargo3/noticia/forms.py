from .models import Asunto, MensajeUsuario, TipoNoticia, Noticia
from django import forms
from django.forms import ModelForm

class AsuntoForm(ModelForm):
    class Meta:
        model = Asunto
        fields= "__all__"

class MensajeUsuarioForm(ModelForm):
    class Meta:
        model = MensajeUsuario
        fields= "__all__" # "__all__" trae todas las columnas del modelo: nombre, correo, asunto, motivo, etc

class TipoNoticiaForm(ModelForm):
    class Meta:
        model = TipoNoticia
        fields= "__all__" 

class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields= "__all__"      

class UsuarioLoginForm(forms.Form):
    nombre = forms.CharField(label='Nombre de usuario o email')
    contraseña = forms.CharField(widget=forms.PasswordInput)        
