from django.db import models
from datetime import date
from .validators import validate_present_or_future


class Especialidade(models.Model):
    nome = models.CharField(max_length=256)

    def __str__(self):
        return self.nome


class Medico(models.Model):
    nome = models.CharField(max_length=256)
    crm = models.CharField(max_length=16)
    email = models.EmailField(max_length=256, blank=True)
    telefone = models.CharField(max_length=13, blank=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE,
                                      blank=True, null=True)

    def __str__(self):
        return self.nome


class Horario(models.Model):
    hora = models.TimeField()

    def __str__(self):
        return self.hora.__str__()


class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia = models.DateField(default=date.today, validators=[validate_present_or_future])
    horarios = models.ManyToManyField(Horario, blank=True)

    # Restrição: uma agenda por dia por médico
    class Meta:
        unique_together = (('medico', 'dia'),)
        index_together = (('medico', 'dia'),)

    def __str__(self):
        return f'{self.medico.nome} {self.dia.__str__()}'


class Consulta(models.Model):
    dia = models.DateField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    horario = models.TimeField()
    data_agendamento = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.medico.nome} {self.dia.__str__()}'
