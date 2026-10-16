from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_inmueble_view, name='crear_inmueble'),
    path('editar/<int:inmueble_id>/', views.editar_inmueble_view, name='editar_inmueble'),
    path('eliminar/<int:inmueble_id>/', views.eliminar_inmueble_view, name='eliminar_inmueble'),
    path('inmuebles/', views.listar_inmuebles_view, name='listar_inmuebles'),
]