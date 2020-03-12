from django.db import models
from django.urls import reverse

# Create your models here.

class Asignatura(models.Model):
	codigo			= models.CharField(max_length=20)
	nombre			= models.CharField(max_length=80)
	semestre		= models.PositiveIntegerField(null=True, blank=True)
	profesor		= models.CharField(max_length=40, null=True, blank=True)
	correo			= models.CharField(max_length=80, null=True, blank=True)

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse("asistencia:asignatura-detail", kwargs={"id": self.id})

class Justificacion(models.Model):
	nombre 			= models.CharField(max_length=40)
	apellidoP 		= models.CharField(max_length=40)
	apellidoM		= models.CharField(max_length=40)
	correo			= models.CharField(max_length=80)
	generacion		= models.PositiveIntegerField()
	rut 			= models.CharField(max_length=10)
	diaInicio		= models.DateField()
	diaFin			= models.DateField()
	motivo			= models.CharField(max_length=255)
	asignatura		= models.ManyToManyField('Asignatura')
	justificativo	= models.FileField(upload_to='justificativos/')
	estado			= models.PositiveIntegerField() # 0 = pendiente, 1 = aceptado, 2 = rechazado

	def get_absolute_url(self):
		return reverse("asistencia:justificacion-detail", kwargs={"id": self.id})