from django.db import models

# Create your models here.
class Senadores(models.Model):
	nome = models.CharField(max_length=40)
	ano_inicio = models.IntegerField(default=2018)
	ano_fim = models.IntegerField(default=2018)
	sexo = models.CharField(max_length=20)

class Governadores(models.Model):
	nome = models.CharField(max_length=40)
	ano_inicio = models.IntegerField(default=2018)
	ano_fim = models.IntegerField(default=2022)
	sexo = models.CharField(max_length=20)
