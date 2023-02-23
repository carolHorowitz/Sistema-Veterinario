from django.db import models

class Dados (models.Model):
    data_atendimento = models.DateTimeField()
    nome_tutor = models.CharField(max_length = 100)
    nome_animal = models.CharField(max_length = 100)
    especie = models.CharField(max_length = 100)
    raca = models.CharField(max_length = 100)
    idade = models.CharField(max_length = 100)
    
class Prontuário (models.Model):
    anotacoes = models.CharField(max_length = 10000)
    data_retorno = models.DateTimeField()    
    
