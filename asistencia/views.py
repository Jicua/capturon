import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import AsignaturaForm, JustificacionForm
from .models import Asignatura, Justificacion

# Create your views here.

############### ASIGNATURAS ################

@login_required
def asignatura_list_page(request):
	queryset = Asignatura.objects.all()
	context = {"object_list": queryset}
	return render(request, "asignatura/list.html", context)

@login_required
def asignatura_create_page(request):
	form = AsignaturaForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = AsignaturaForm()
		return redirect('./')
	context = {
		"form": form
	}
	return render(request, "asignatura/create.html", context)

@login_required
def asignatura_update_page(request, id):
	obj = get_object_or_404(Asignatura, id=id)
	form = AsignaturaForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
		form = AsignaturaForm()
		return redirect(obj.get_absolute_url())
	context = {
		"form": form
	}
	return render(request, "asignatura/create.html", context)

@login_required
def asignatura_detail_page(request, id):
	obj = get_object_or_404(Asignatura, id=id)
	context = {
		"asignatura": obj
		}
	return render(request, "asignatura/detail.html", context)

@login_required
def asignatura_delete_page(request, id):
	obj = get_object_or_404(Asignatura, id=id)
	if request.method == "POST":
		obj.delete()
		return redirect('../../')
	context = {
		"asignatura": obj
	}
	return render(request, "asignatura/delete.html", context)

############### JUSTIFICACION ################

@login_required
def justificacion_aprobar_page(request, id):
	obj = get_object_or_404(Justificacion, id=id)
	form = JustificacionForm(request.POST or None, request.FILES or None, instance=obj)
	if form.is_valid():
		form.save()
		form = JustificacionForm()
		return redirect('../')
	context = {
		"form": form,
		"obj": obj
	}
	return render(request, "justificacion/aprobar.html", context)

@login_required
def justificacion_rechazar_page(request, id):
	obj = get_object_or_404(Justificacion, id=id)
	form = JustificacionForm(request.POST or None, request.FILES or None, instance=obj)
	if form.is_valid():
		form.save()
		form = JustificacionForm()
		return redirect('../')
	context = {
		"form": form,
		"obj": obj
	}
	return render(request, "justificacion/rechazar.html", context)

@login_required
def justificacion_list_page(request):
	queryset = Justificacion.objects.all().order_by('estado', 'mesInicio', 'diaInicio')
	context = {"object_list": queryset}
	return render(request, "justificacion/list.html", context)

@login_required
def justificacion_detail_page(request, id):
	obj = get_object_or_404(Justificacion, id=id)
	asignaturas = obj.asignatura.all()
	context = {
		"justificacion": obj,
		"asignaturas": asignaturas
		}
	return render(request, "justificacion/detail.html", context)

def justificacion_create_page(request):
	form = JustificacionForm(request.POST or None, request.FILES or None)
	asignaturas = Asignatura.objects.all()
	now = datetime.datetime.now()
	anyoActual = now.year
	anyos = []
	i = 0
	while i < 8:
		anyos.append(anyoActual - i)
		i+=1
	if form.is_valid():
		form.save()
		form = JustificacionForm()
		return redirect('./')
	context = {
		"form": form,
		"asignaturas": asignaturas,
		"anyos": anyos
	}
	return render(request, "justificacion/create.html", context)

@login_required
def justificacion_update_page(request, id=id):
	obj = get_object_or_404(Justificacion, id=id)
	form = JustificacionForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
		form = JustificacionForm()
		return redirect('../')
	context = {"form": form}
	return render(request, "justificacion/create.html", context)

@login_required
def justificacion_delete_page(request, id):
	obj = get_object_or_404(Justificacion, id=id)
	if request.method == "POST":
		obj.delete()
		return redirect('../../')
	context = {"object": obj}
	return render(request, "justificacion/delete.html", context)