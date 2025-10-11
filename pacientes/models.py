from django.db import models

class Paciente(models.Model):
    rut = models.CharField(max_length=12, unique=True)  # RUT chileno o identificador
    apellidos = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    hora_consulta = models.TimeField()
    diagnostico = models.CharField(max_length=255)
    doctor = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)  # Ejemplo: "gripal", "recuperado", etc.

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.rut}"