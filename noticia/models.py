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
    correo = models.EmailField(unique=True, max_length=40, null=False)
    asunto = models.ForeignKey(Asunto, on_delete=models.CASCADE, db_column='idAsunto', null=True)
    motivo = models.TextField(max_length=300, null=False)

    def __str__(self):
        return str(self.correo)
