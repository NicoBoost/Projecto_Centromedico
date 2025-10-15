import requests
from django.shortcuts import render, redirect

API_URL = 'http://127.0.0.1:8000/api/pacientes/'  # Ajustar según tu API

# ------------------------------
# Vista principal
# ------------------------------
def index(request):
    return render(request, 'index.html')


# ------------------------------
# Registrar paciente
# ------------------------------
def registrar(request):
    if request.method == 'POST':
        data = {
            "rut": request.POST['rut'],
            "apellidos": request.POST['apellidos'],
            "nombres": request.POST['nombres'],
            "fecha_nacimiento": request.POST['fecha_nacimiento'],
            "hora_consulta": request.POST['hora_consulta'],
            "diagnostico": request.POST['diagnostico'],
            "doctor": request.POST['doctor'],
            "estado": request.POST['estado']
        }
        response = requests.post(API_URL, json=data)
        if response.status_code == 201:
            return redirect('listar')
    return render(request, 'registrar.html')


# ------------------------------
# Listar pacientes
# ------------------------------
def listar(request):
    response = requests.get(API_URL)
    pacientes = response.json() if response.status_code == 200 else []
    return render(request, 'listar.html', {'pacientes': pacientes})


# ------------------------------
# Editar paciente
# ------------------------------
def editar(request, id):
    paciente_url = f"{API_URL}{id}/"
    if request.method == 'POST':
        data = {
            "rut": request.POST['rut'],
            "apellidos": request.POST['apellidos'],
            "nombres": request.POST['nombres'],
            "fecha_nacimiento": request.POST['fecha_nacimiento'],
            "hora_consulta": request.POST['hora_consulta'],
            "diagnostico": request.POST['diagnostico'],
            "doctor": request.POST['doctor'],
            "estado": request.POST['estado']
        }
        response = requests.put(paciente_url, json=data)
        if response.status_code in [200, 204]:
            return redirect('listar')
    
    response = requests.get(paciente_url)
    paciente = response.json() if response.status_code == 200 else {}
    return render(request, 'editar.html', {'paciente': paciente})

# ------------------------------
# Pacientes Gripales
# ------------------------------
def pacientes_gripales(request):
    """
    Consulta la API para traer solo pacientes con estado gripal
    """
    try:
        response = requests.get(f'{API_URL}estado_gripal/')     # endpoint personalizado
        response.raise_for_status()                             # lanza excepción si hay error
        pacientes = response.json()                             # lista de diccionarios
    except requests.RequestException as e:
        print("Error al consultar la API:", e)
        pacientes = []                                          # fallback: lista vacía

    return render(request, 'pacientes_gripales.html', {'pacientes': pacientes})


# ------------------------------
# Eliminar paciente
# ------------------------------
def eliminar(request, id):
    paciente_url = f"{API_URL}{id}/"
    if request.method == 'POST':
        requests.delete(paciente_url)
        return redirect('listar')
    
    # Para confirmación podrías mostrar info del paciente
    response = requests.get(paciente_url)
    paciente = response.json() if response.status_code == 200 else {}
    return render(request, 'eliminar.html', {'paciente': paciente})
