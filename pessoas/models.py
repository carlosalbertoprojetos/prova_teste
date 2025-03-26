from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers, viewsets, routers
from django.urls import path, include


class Pessoa(models.Model):
    class SexoChoices(models.TextChoices):
        MASCULINO = "M", _("Masculino")
        FEMININO = "F", _("Feminino")

    nome = models.CharField(max_length=255)
    data_nasc = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    sexo = models.CharField(max_length=1, choices=SexoChoices.choices)
    altura = models.FloatField()
    peso = models.FloatField()

    def calcular_peso_ideal(self):
        if self.sexo == self.SexoChoices.MASCULINO:
            return (72.7 * self.altura) - 58
        elif self.sexo == self.SexoChoices.FEMININO:
            return (62.1 * self.altura) - 44.7
        return None

    def __str__(self):
        return self.nome
