from django.db import models

# Create your models here.
class Medico(models.Model):
    rut_medico = models.CharField(primary_key=True, max_length=20)
    nombre_medico = models.CharField(max_length=30)

    def __str__(self):
        return self.rut_medico


class Paciente(models.Model):
    rut_paciente = models.CharField(primary_key=True, max_length=20)
    nombre_paciente = models.CharField(max_length=30)
    sexo_paciente = models.CharField(max_length=15)
    edad_paciente = models.IntegerField()

    def __str__(self):
        return self.rut_paciente


class FichaMedica(models.Model):
    nombre_medicamento = models.CharField(max_length=30)
    rut_medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    rut_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    observacion_paciente = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_medicamento