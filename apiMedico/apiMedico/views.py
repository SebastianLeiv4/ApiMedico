from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from consultaMedica.models import Medico, Paciente, FichaMedica
from apiMedico.serializers import MedicoSerializer, PacienteSerializer, FichaMedicaSerializer


class MedicoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer



class PacienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer



class FichaMedicaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = FichaMedica.objects.all()
    serializer_class = FichaMedicaSerializer