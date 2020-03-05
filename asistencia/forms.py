import re
from django import forms
from .models import Asignatura, Justificacion

class AsignaturaForm(forms.ModelForm):
	class Meta:
		model = Asignatura
		fields = [
			'codigo',
			'nombre',
			'semestre'
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
