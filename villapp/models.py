from django.db import models
from django.contrib.auth.models import User

class Usuario (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.user.username

class Casa(models.Model):
    numero_de_casa = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    descripcion = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def __str__(self):
        return self.numero_de_casa

class Mes(models.Model):
    Mes = {
        ('Enero', 'Enero'),
        ('Febrero', 'Febrero'),
        ('Marzo', 'Marzo'),
        ('Abril', 'Abril'),
        ('Mayo', 'Mayo'),
        ('Junio', 'Junio'),
        ('Julio', 'Julio'),
        ('Agosto', 'Agosto'),
        ('Septiembre', 'Septiembre'),
        ('Octubre', 'Octubre'),
        ('Noviembre', 'Noviembre'),
        ('Diciembre', 'Diciembre'),
    }

    mes = models.CharField(max_length=100, choices=Mes)
    anio = models.IntegerField()
    def __str__(self):
        return self.mes

class PagoRealizado (models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    pago = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.usuario.user.username