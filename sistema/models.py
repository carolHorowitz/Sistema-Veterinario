from django.db import models

class Dados (models.Model):
    
    nome_tutor = models.CharField(max_length = 100)
    nome_animal = models.CharField(max_length = 100)
    especie = models.CharField(max_length = 100)
    raca = models.CharField(max_length = 100)
    idade = models.CharField(max_length = 100)
    data_atendimento = models.DateField()
    
    class Meta:
        verbose_name = 'Dado'
        
    def __str__(self):
        return self.nome_tutor   
    
class Prontuario (models.Model):
    anotacoes = models.CharField(max_length = 10000)
    data_retorno = models.DateField()
    
    class Meta:
        verbose_name = 'Prontuario' 
        
    def __str__(self):
        return self.nome_tutor
    
class Usuario (models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField() 
    senha = models.CharField(max_length=64)
     
    def __str__ (self):
        return self.nome        
    
