from rest_framework import serializers
from .models import Especialidade, Medico, Horario, Agenda, Consulta
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_date):
        user = User.objects.create_user(**validated_date)
        Token.objects.create(user=user)
        return user


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
