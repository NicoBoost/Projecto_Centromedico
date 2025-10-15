from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h2>Bienvenido a la API del Centro Médico</h2><p>Visita <a href='/api/pacientes/'>/api/pacientes/</a> para ver los pacientes.</p>")

urlpatterns = [
    #path('', home),
    path('admin/', admin.site.urls),
    path('', include('pacientes.urls')),            # Front-end
    path('api/', include('pacientes.api.urls')),    # API rest
]
