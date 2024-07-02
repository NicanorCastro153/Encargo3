from .models import Asunto, MensajeUsuario
from django.forms import ModelForm

class AsuntoForm(ModelForm):
    class Meta:
        model = Asunto
        fields= "__all__"

class MensajeUsuarioForm(ModelForm):
    class Meta:
        model = MensajeUsuario
        fields= "__all__"
