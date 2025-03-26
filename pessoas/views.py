from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Pessoa


def index(request):
    return render(request, "index.html")


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = "__all__"


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

    def calcular_peso_ideal(self, request, pk=None):
        pessoa = self.get_object()
        peso_ideal = pessoa.calcular_peso_ideal()
        return Response({"peso_ideal": peso_ideal})
