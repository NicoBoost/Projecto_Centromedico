from django.urls import path
from pacientes.api.views import PacienteListCreate, PacienteDetail

urlpatterns = [
    path('pacientes/', PacienteListCreate.as_view(), name='api_pacientes_list'),
    path('pacientes/<int:pk>/', PacienteDetail.as_view(), name='api_pacientes_detail'),
]

