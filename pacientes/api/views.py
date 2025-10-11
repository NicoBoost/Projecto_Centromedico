from rest_framework import viewsets
from pacientes.models import Paciente
from .serializers import PacienteSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    # Consulta personalizada: pacientes con estado gripal
    @action(detail=False, methods=['get'])
    def estado_gripal(self, request):
        pacientes_gripales = Paciente.objects.filter(estado__iexact='gripal')
        serializer = self.get_serializer(pacientes_gripales, many=True)
        return Response(serializer.data)
