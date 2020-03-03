from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import AsignaturaForm, JustificacionForm
from .models import Asignatura, Justificacion

# Create your views here.

############### ASIGNATURAS ################
 
def asignatura_list_page(request):
	queryset = Asignatura.objects.all()
	context = {"object_list": queryset}
	return render(request, "asignatura/list.html", context)

def asignatura_create_page(request):
	form = AsignaturaForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = AsignaturaForm()
		return redirect('./')
	context = {"form": form}
	return render(request, "asignatura/create.html", context)

############### JUSTIFICACION ################

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

def justificacion_list_page(request):
	queryset = Justificacion.objects.all()
	context = {"object_list": queryset}
	return render(request, "justificacion/list.html", context)

def justificacion_detail_page(request, id):
	obj = get_object_or_404(Justificacion, id=id)
	context = {"justificacion": obj}
	return render(request, "justificacion/detail.html", context)

def justificacion_create_page(request):
	form = JustificacionForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		form = JustificacionForm()
		return redirect('./')
	context = {"form": form}
	return render(request, "justificacion/create.html", context)

def justificacion_update_page(request, id=id):
	obj = get_object_or_404(Justificacion, id=id)
	form = JustificacionForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
		form = JustificacionForm()
		return redirect('../')
	context = {"form": form}
	return render(request, "justificacion/create.html", context)

def justificacion_delete_page(request, id):
	obj = get_object_or_404(Justificacion, id=id)
	if request.method == "POST":
		obj.delete()
		return redirect('../../')
	context = {"object": obj}
	return render(request, "justificacion/delete.html", context)