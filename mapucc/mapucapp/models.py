from django.db import models

# Create your models here.
class Local(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    predio = models.CharField(max_length=50)
    sala = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome