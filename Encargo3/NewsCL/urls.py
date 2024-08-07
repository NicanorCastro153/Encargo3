"""
URL configuration for NewsCL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from noticia import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('noticia/',include('noticia.urls')),
    path('', include('noticia.urls')),
    path('logout/', views.logout_view, name='logout'),
    path('Iniciar_sesion/', views.Iniciar_sesion, name='Iniciar_sesion'),\
]

# config de ruta de carpeta media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)