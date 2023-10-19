from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    inscriptos = models.IntegerField()
    TURNOS = (
        (1, "Mañana"),
        (2, "Tarde"),
        (3, "Noche"),
    )
    turno = models.IntegerField(choices=TURNOS, default=1)  

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    monotributista = models.BooleanField()
    
    class Meta:
        verbose_name="Docente"
        verbose_name_plural="Docentes"

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
