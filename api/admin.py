from django.contrib import admin
from .models import (Especialidade,
                     Medico,
                     Horario,
                     Agenda,
                     Consulta)


admin.site.register(Especialidade)
admin.site.register(Medico)
admin.site.register(Horario)
admin.site.register(Agenda)
admin.site.register(Consulta)
