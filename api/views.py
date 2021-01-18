from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .filters import MedicoFilter
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User


from .models import (Especialidade,
                     Medico,
                     Consulta,
                     Horario,
                     Agenda)

from .serializers import (EspecialidadeSerializer,
                          MedicoSerializer,
                          ConsultaSerializer,
                          AgendaSerializer,
                          UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filterset_class = MedicoFilter
    authentication_classes = (TokenAuthentication,)


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    filter_fields = ('dia',)

    # Sobrescrever POST com os requesitos desejado
    # def create(self, request, *args, **kwargs):
    #     if 'agenda_id' in request.data and 'horario' in request.data:
    #         agenda = Agenda.objects.get(id=request.data['agenda_id'])
    #         horario = Horario.objects.get(hora=request.data['horario'])
    #         response = {'message': 'es jay!'}
    #         return Response(response, status=status.HTTP_200_OK)
    #     else:
    #         response = {'message': 'es jay!'}
    #         return Response(response, status=status.HTTP_400_BAD_REQUEST)

