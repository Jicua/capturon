from django.urls import path
from django.urls import path, include

from .views import (
	asignatura_list_page,
	asignatura_create_page,

	justificacion_detail_page,
	justificacion_list_page,
	justificacion_create_page,
	justificacion_update_page,
	justificacion_delete_page,
	justificacion_aprobar_page,
	justificacion_rechazar_page
	)

app_name = "asistencia"

urlpatterns = [
	path('asignatura/', asignatura_list_page, name='asignatura-list'),
	path('asignatura/crear/', asignatura_create_page, name='asignatura-create'),

 	path('justificacion/', justificacion_list_page, name='justificacion-list'),
 	path('justificacion/crear/', justificacion_create_page, name='justificacion-create'),
    path('justificacion/<int:id>/', justificacion_detail_page, name='justificacion-detail'),
 	path('justificacion/<int:id>/editar/', justificacion_update_page, name='justificacion-update'),
 	path('justificacion/<int:id>/eliminar/', justificacion_delete_page, name='justificacion-delete'), 
 	path('justificacion/<int:id>/aprobar', justificacion_aprobar_page, name='justificacion-aprobar'),
 	path('justificacion/<int:id>/rechazar', justificacion_rechazar_page, name='justificacion-rechazar')
]