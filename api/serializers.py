from rest_framework import serializers
from .models import Especialidade, Medico, Horario, Agenda, Consulta


class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = ['id', 'nome']


class MedicoSerializer(serializers.ModelSerializer):

    especialidade = EspecialidadeSerializer(read_only=True)

    class Meta:
        model = Medico
        fields = ['id', 'nome', 'crm', 'especialidade']


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ['hora']


# Implementar serializador que retora lista de horarios como lista de stings
# class HorarioAsStringList(serializers.Serializer):

class AgendaSerializer(serializers.ModelSerializer):

    horarios = HorarioSerializer(many=True)

    class Meta:
        model = Agenda
        fields = ['id', 'medico', 'dia', 'horarios']


class ConsultaSerializer(serializers.ModelSerializer):

    medico = MedicoSerializer()

    class Meta:
        model = Consulta
        fields = ['id', 'dia', 'horario', 'data_agendamento', 'medico']
