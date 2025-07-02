from django.contrib import admin
from django.urls import path
from app.views import (
    IndexView,
    PacienteListView,
    MedicoListView,
    EnfermeiroListView,
    PrescricaoListView,
    MedicamentoListView,
    AdministracaoListView,
    AlertaListView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('pacientes/', PacienteListView.as_view(), name='pacientes'),
    path('medicos/', MedicoListView.as_view(), name='medicos'),
    path('enfermeiros/', EnfermeiroListView.as_view(), name='enfermeiros'),
    path('prescricoes/', PrescricaoListView.as_view(), name='prescricoes'),
    path('medicamentos/', MedicamentoListView.as_view(), name='medicamentos'),
    path('administracoes/', AdministracaoListView.as_view(), name='administracoes'),
    path('alertas/', AlertaListView.as_view(), name='alertas'),
]
