
from django.urls import path
from . import views

urlpatterns = [
    #opciones navbar
    path('home',views.home, name='home'),
    path('actualidad',views.actualidad, name='actualidad'),
    path('contactanos',views.contactanos, name='contactanos'),
    path('deporte',views.deporte, name='deporte'),
    path('economia',views.economia, name='economia'),
    #noticias
    path('noticiaArsenal',views.noticiaArsenal, name='noticiaArsenal'),
    path('noticiaBasketball',views.noticiaBasketball, name='noticiaBasketball'),
    path('noticiaEconomia',views.noticiaEconomia, name='noticiaEconomia'),
    path('noticiaEncerrona',views.noticiaEncerrona, name='noticiaEncerrona'),
    path('noticiaMonroe',views.noticiaMonroe, name='noticiaMonroe'),
    path('noticiaNintendo',views.noticiaNintendo, name='noticiaNintendo'),
    path('noticiaTenis',views.noticiaTenis, name='noticiaTenis'),
    path('noticiaLula',views.noticiaLula, name='noticiaLula'),
    path('noticiaEli',views.noticiaeli, name='noticiaeli'),
]