from rest_framework import serializers
from .models import Pessoa


class PessoaSerializer(serializers.ModelSerializer):
    peso_ideal = serializers.SerializerMethodField()

    class Meta:
        model = Pessoa
        fields = ["nome", "data_nasc", "cpf", "sexo", "altura", "peso"]
        extra_kwargs = {
            "nome": {"required": True},
            "data_nasc": {"required": True},
            "cpf": {"required": True},
            "sexo": {"required": True},
            "altura": {"required": True},
            "peso": {"required": True},
        }

    # def get_peso_ideal(self, obj):
    #     return obj.calcular_peso_ideal()
