from django_filters import rest_framework as filters
from .models import Medico


class MedicoFilter(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Medico
        fields = ['especialidade']