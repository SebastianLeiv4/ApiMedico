from rest_framework import serializers
from consultaMedica.models import  Medico, Paciente, FichaMedica


class MedicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medico
        fields = ['url', 'rut_medico', 'nombre_medico']


class PacienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paciente
        fields = ['url', 'rut_paciente', 'nombre_paciente', 'sexo_paciente', 'edad_paciente']


class FichaMedicaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FichaMedica
        fields = ['url', 'nombre_medicamento', 'rut_medico', 'rut_paciente', 'observacion_paciente']