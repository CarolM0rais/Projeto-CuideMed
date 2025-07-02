from django.views import View
from django.shortcuts import render
from .models import Paciente, Medico, Enfermeiro, Prescricao, Medicamento, Administracao, Alerta

# Página inicial
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

# Lista de Pacientes
class PacienteListView(View):
    def get(self, request):
        pacientes = Paciente.objects.all()
        return render(request, 'pacientes.html', {'pacientes': pacientes})

# Lista de Médicos
class MedicoListView(View):
    def get(self, request):
        medicos = Medico.objects.all()
        return render(request, 'medicos.html', {'medicos': medicos})

# Lista de Enfermeiros
class EnfermeiroListView(View):
    def get(self, request):
        enfermeiros = Enfermeiro.objects.all()
        return render(request, 'enfermeiros.html', {'enfermeiros': enfermeiros})

# Lista de Prescrições
class PrescricaoListView(View):
    def get(self, request):
        prescricoes = Prescricao.objects.all()
        return render(request, 'prescricoes.html', {'prescricoes': prescricoes})

# Lista de Medicamentos
class MedicamentoListView(View):
    def get(self, request):
        medicamentos = Medicamento.objects.all()
        return render(request, 'medicamentos.html', {'medicamentos': medicamentos})

# Lista de Administrações de Medicamentos
class AdministracaoListView(View):
    def get(self, request):
        administracoes = Administracao.objects.all()
        return render(request, 'administracoes.html', {'administracoes': administracoes})

# Lista de Alertas
class AlertaListView(View):
    def get(self, request):
        alertas = Alerta.objects.all()
        return render(request, 'alertas.html', {'alertas': alertas})
