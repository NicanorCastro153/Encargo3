from django.db import models

# Create your models here.
class Asunto(models.Model):
    id_asunto = models.AutoField(db_column='idAsunto', primary_key=True)
    asunto = models.CharField(max_length=40)

    def __str__(self):
        return str(self.asunto)

class MensajeUsuario(models.Model):
    id_mensaje = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=20, null=True)
    correo = models.EmailField(max_length=40, null=False)
    asunto = models.ForeignKey(Asunto, on_delete=models.CASCADE, db_column='idAsunto', null=True)
    motivo = models.TextField(max_length=300, null=False)

    def __str__(self):
        return str(self.correo)


#Actualidad, Deportes, Economia, etc
class TipoNoticia(models.Model):
    id_tipo = models.AutoField(db_column='idTipo',primary_key=True)
    tipo = models.CharField(max_length=25,blank=False,null=False)  

    def __str__(self):
        return str(self.tipo)

class Noticia(models.Model):
    id_noticia = models.AutoField(primary_key=True,null=False)
    titulo = models.CharField(max_length=40,blank=False,null=False)
    descripcion = models.TextField(max_length=200,default='')
    tipo = models.ForeignKey(TipoNoticia,on_delete=models.CASCADE,db_column='idTipo',null=False)
    imagen = models.ImageField(upload_to='images/',null=False)

    def __str__(self):
        return str(self.titulo)
    
    
from django.db import models
from django.contrib.auth.models import User

class Suscripcion(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='suscripciones/')
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.titulo

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    suscripcion = models.ForeignKey(Suscripcion, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.usuario.username} - {self.suscripcion.titulo}"

    

    
    
