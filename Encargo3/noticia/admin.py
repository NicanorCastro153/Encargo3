from django.contrib import admin
from .models import Asunto, MensajeUsuario, TipoNoticia, Noticia, Suscripcion
# modelos

admin.site.register(Asunto)
admin.site.register(MensajeUsuario)
admin.site.register(TipoNoticia)
admin.site.register(Noticia)
admin.site.register(Suscripcion)





