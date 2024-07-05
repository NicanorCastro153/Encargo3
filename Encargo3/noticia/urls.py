
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('actualidad', views.actualidad, name='actualidad'),
    path('contactanos', views.contactanos, name='contactanos'),
    path('deporte', views.deporte, name='deporte'),
    path('economia', views.economia, name='economia'),
    path('ultimas_noticias', views.ultimas_noticias, name='ultimas_noticias'),
    path('noticiaArsenal', views.noticiaArsenal, name='noticiaArsenal'),
    path('noticiaBasketball', views.noticiaBasketball, name='noticiaBasketball'),
    path('noticiaEconomia', views.noticiaEconomia, name='noticiaEconomia'),
    path('noticiaEncerrona', views.noticiaEncerrona, name='noticiaEncerrona'),
    path('noticiaMonroe', views.noticiaMonroe, name='noticiaMonroe'),
    path('noticiaNintendo', views.noticiaNintendo, name='noticiaNintendo'),
    path('noticiaTenis', views.noticiaTenis, name='noticiaTenis'),
    path('noticiaLula', views.noticiaLula, name='noticiaLula'),
    path('noticiaEli', views.noticiaeli, name='noticiaeli'),
    path('AgregarNoticia', views.AgregarNoticia, name='AgregarNoticia'),
    path('AgregarTipoNoticia', views.AgregarTipoNoticia, name='AgregarTipoNoticia'),
    path('AgregarAsunto', views.AgregarAsunto, name='AgregarAsunto'),
    path('Contactanos', views.Contactanos, name='Contactanos'),
    path('Iniciar_sesion', views.Iniciar_sesion, name='Iniciar_sesion'),
    path('registrar', views.registrar, name='registrar'),
    path('PanelAdministrador', views.PanelAdministrador, name='PanelAdministrador'),
    path('noticia_del/<str:pk>', views.noticia_del, name='noticia_del'),
]