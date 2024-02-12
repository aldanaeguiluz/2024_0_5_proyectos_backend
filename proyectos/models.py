from django.db import models

# Create your models here.
class Usuario(models.Model):
    username= models.CharField(max_length=20)
    password= models.CharField(max_length=20)
    nombre= models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Equipo(models.Model):
    EQUIPO_ESTADOS=(
        ("A","Activo"),
        ("I", "Inactivo")
    )

    nombre= models.CharField(max_length=20)
    anho= models.IntegerField(verbose_name="año", null=True)
    estado=models.CharField(max_length=1, choices=EQUIPO_ESTADOS)
    
    def __str__(self):
        return self.nombre
    