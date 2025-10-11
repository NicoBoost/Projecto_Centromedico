# Proyecto Centro Médico

Este proyecto es un sistema de gestión de pacientes para un centro médico, desarrollado en **Django** y consumiendo una **API REST** para las operaciones de pacientes (CRUD). Además, utiliza **Materialize CSS** para el front-end y es responsive.

## Funcionalidades

- Registrar pacientes nuevos.
- Listar todos los pacientes existentes.
- Actualizar información de pacientes.
- Eliminar pacientes.
- Navegación adaptable a dispositivos móviles.
- Interfaz limpia basada en Materialize CSS.

## Formato de datos (API)

La API maneja los pacientes con el siguiente formato JSON:

```json
{
    "id": 1,
    "rut": "12345657-8",
    "apellidos": "Pérez",
    "nombres": "Juan",
    "fecha_nacimiento": "2000-01-01",
    "hora_consulta": "20:00:00",
    "diagnostico": "Faringitis Aguda",
    "doctor": "Melo Tirra",
    "estado": "Vivo"
}

## Instalación

Clonar el repositorio:

git clone https://github.com/NicoBoost/Projecto_Centromedico.git
cd Projecto_Centromedico


Crear y activar un entorno virtual:

python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows


Instalar dependencias:

pip install -r requirements.txt


Ejecutar migraciones:

python manage.py migrate


Ejecutar el servidor:

python manage.py runserver


Acceder a la aplicación en:

http://127.0.0.1:8000/

## Estructura de archivos

pacientes/ → App principal con modelos, vistas y templates.

pacientes/templates/ → Contiene los templates HTML.

pacientes/static/ → Archivos CSS y JS.

pacientes/api/ → API REST para la gestión de pacientes.

## Tecnologías utilizadas

Python 3.13

Django 5.2

Django REST Framework

Materialize CSS

SQLite (Base de datos)

## Autor

Nicolás Martinez
GitHub: NicoBoost
