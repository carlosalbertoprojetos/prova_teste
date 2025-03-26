from django.db import models


class Pessoa(models.Model):
    SEXO_CHOICES = [
        ("M", "Masculino"),
        ("F", "Feminino"),
    ]

    nome = models.CharField(max_length=255)
    data_nasc = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    altura = models.FloatField()
    peso = models.FloatField()

    def calcular_peso_ideal(self):
        if self.sexo == "M":
            return (72.7 * self.altura) - 58
        else:
            return (62.1 * self.altura) - 44.7

    def __str__(self):
        return self.nome
