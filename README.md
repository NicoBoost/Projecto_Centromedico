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
