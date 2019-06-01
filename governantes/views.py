from django.shortcuts import render, redirect
from .models import Senadores, Governadores
from .forms import FormularioSenadores
# Create your views here.

def listar_senadores(request):
	senadores = Senadores.objects.all()
	return render(request, 'senadores.html', {"lista_senadores":senadores})
def listar_governadores(request):
	governadores = Governadores.objects.all()
	return render(request, 'governadores.html', {"lista_governadores":governadores})

def inicio(request):
	return render(request, 'index.html')

def formulario(request):
	if request.method == 'POST':
		form = FormularioSenadores(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
		return redirect('/listar/senadores')
	else:
		form = FormularioSenadores()
	return render(request, 'cadastro_senadores.html', {'form':form})