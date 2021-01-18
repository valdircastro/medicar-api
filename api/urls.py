from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# ViewSets imports
from .views import (EspecialidadeViewSet,
                    MedicoViewSet,
                    AgendaViewSet,
                    ConsultaViewSet,
                    UserViewSet)

router = routers.DefaultRouter()
router.register('especialidades', EspecialidadeViewSet)
router.register('medicos', MedicoViewSet)
router.register('agendas', AgendaViewSet)
router.register('consultas', ConsultaViewSet)
router.register('usuarios', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
