from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar/', views.registrar, name='registrar'),
    path('listar/', views.listar, name='listar'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('pacientes_gripales/', views.pacientes_gripales, name='pacientes_gripales'),
]
