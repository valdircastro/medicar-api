from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# ViewSets imports
from .views import (EspecialidadeViewSet,
                    MedicoViewSet,
                    AgendaViewSet,
                    ConsultaViewSet)

router = routers.DefaultRouter()
router.register('especialidades', EspecialidadeViewSet)
router.register('medicos', MedicoViewSet)
router.register('agendas', AgendaViewSet)
router.register('consultas', ConsultaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
