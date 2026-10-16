from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('elegir-tipo/', views.elegir_tipo_usuario_view, name='elegir_tipo_usuario'),
    path('crear-perfil/<str:tipo>/', views.crear_perfil_view, name='crear_perfil'),
]