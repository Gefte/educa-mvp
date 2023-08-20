from django.db import models

class Questao(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    url = models.URLField(null=False, blank=False)  # Use URLField for URLs
    foto = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return f"Questao [nome={self.nome}]"
    
class Materia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    url = models.URLField(null=False, blank=False)  # Use URLField for URLs
    
    def __str__(self):
        return f"Nome da materia [nome={self.nome}]"