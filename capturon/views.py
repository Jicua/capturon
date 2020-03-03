from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
	context = {
	"title": "CAPTURON"
	}
	return render(request, "home.html", context)

def contacto_page(request):
	return render(request, "contacto.html", {})