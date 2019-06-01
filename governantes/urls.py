from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
	path('listar/senadores', views.listar_senadores),
	path('novo/senador', views.formulario),
	path('listar/governadores', views.listar_governadores),
	path('', views.inicio),
]