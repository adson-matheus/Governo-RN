from django import forms
from .models import Senadores

class FormularioSenadores(forms.ModelForm):
	class Meta:
		model = Senadores
		fields = ('nome', 'ano_inicio', 'ano_fim', 'sexo',)    
