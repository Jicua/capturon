from django.db import models
from django.urls import reverse

# Create your models here.

class Asignatura(models.Model):
	codigo			= models.CharField(max_length=20)
	nombre			= models.CharField(max_length=40)
	semestre		= models.PositiveIntegerField()

	def __str__(self):
		return self.nombre

class Justificacion(models.Model):
	nombre 			= models.CharField(max_length=40)
	apellidoP 		= models.CharField(max_length=40)
	apellidoM		= models.CharField(max_length=40)
	correo			= models.CharField(max_length=80)
	generacion		= models.PositiveIntegerField()
	rut 			= models.CharField(max_length=10)
	diaInicio		= models.PositiveIntegerField()
	mesInicio		= models.PositiveIntegerField()
	diaFin			= models.PositiveIntegerField()
	mesFin			= models.PositiveIntegerField()
	motivo			= models.CharField(max_length=255)
	asignatura		= models.ForeignKey('Asignatura', on_delete=models.CASCADE)
	justificativo	= models.FileField(upload_to='justificativos/')
	estado			= models.PositiveIntegerField() # 0 = pendiente, 1 = aceptado, 2 = rechazado

	def get_absolute_url(self):
		return reverse("asistencia:justificacion-detail", kwargs={"id": self.id})