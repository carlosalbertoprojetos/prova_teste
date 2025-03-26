from django.db import models

from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    data_nasc = models.DateField()
    cpf = models.CharField(max_length=11)
    sexo = models.CharField(
        max_length=1, choices=[("M", "Masculino"), ("F", "Feminino")]
    )
    altura = models.FloatField()
    peso = models.FloatField()

    def __str__(self):
        return self.nome

    # def calcular_peso_ideal(self):
    #     if self.sexo == "M":
    #         return (72.7 * self.altura) - 58
    #     elif self.sexo == "F":
    #         return (62.1 * self.altura) - 44.7
    #     return None
