from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pacientes.api.views import PacienteListCreate, PacienteDetail, PacienteViewSet

router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet, basename='pacientes')

urlpatterns = [
    path('pacientes/', PacienteListCreate.as_view(), name='api_pacientes_list'),
    path('pacientes/<int:pk>/', PacienteDetail.as_view(), name='api_pacientes_detail'),
     path('', include(router.urls)),                                                    # /api/ dará acceso a todas las rutas del ViewSet
]

