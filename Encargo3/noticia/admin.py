from django.contrib import admin
from .models import Asunto, MensajeUsuario, TipoNoticia, Noticia
# modelos

admin.site.register(Asunto)
admin.site.register(MensajeUsuario)
admin.site.register(TipoNoticia)
admin.site.register(Noticia)