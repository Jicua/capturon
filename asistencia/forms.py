import re
from django import forms
from .models import Asignatura, Justificacion

class AsignaturaForm(forms.ModelForm):
	class Meta:
		model = Asignatura
		fields = [
			'codigo',
			'nombre',
			'semestre',
			'profesor',
			'correo'
		]

class JustificacionForm(forms.ModelForm):
	class Meta:
		model = Justificacion
		fields = [
			'nombre',
			'apellidoP',
			'apellidoM',
			'correo',
			'generacion',
			'rut',
			'diaInicio',
			'mesInicio',
			'diaFin',
			'mesFin',
			'motivo',
			'asignatura',
			'justificativo',
			'estado'
		]

	def clean_rut(self, *args, **kwargs):
		rut = self.cleaned_data.get("rut")
		rut = rut.upper()
		valid = re.compile('\d{7,8}-[\dK]')
		if valid.match(rut) == None:
			raise forms.ValidationError("Rut inválido")
		else:
			return rut

	def clean_nombre(self, *args, **kwargs):
		nombre = self.cleaned_data.get("nombre")
		nombre = nombre.title()
		valid = re.compile('[A-Z][a-zA-Z][^#&<>\"~;$^%{}?]{1,40}$')
		if valid.match(nombre) == None:
			raise forms.ValidationError("Nombre inválido")
		else:
			return nombre

	def clean_apellidoP(self, *args, **kwargs):
		apellidoP = self.cleaned_data.get("apellidoP")
		apellidoP = apellidoP.title()
		valid = re.compile('[A-Z][a-zA-Z][^#&<>\"~;$^%{}?]{1,40}$')
		if valid.match(apellidoP) == None:
			raise forms.ValidationError("Apellido paterno inválido")
		else:
			return apellidoP

	def clean_apellidoM(self, *args, **kwargs):
		apellidoM = self.cleaned_data.get("apellidoM")
		apellidoM = apellidoM.title()
		valid = re.compile('[A-Z][a-zA-Z][^#&<>\"~;$^%{}?]{1,40}$')
		if valid.match(apellidoM) == None:
			raise forms.ValidationError("Apellido materno inválido")
		else:
			return apellidoM
