from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Pessoa
from .serializers import PessoaSerializer
from .services import (
    criar_pessoa,
    atualizar_pessoa,
    excluir_pessoa,
    obter_pessoa_por_id,
)
from .tasks import calcular_peso_ideal


def index(request):
    return render(request, "pessoas/index.html")


class PessoaViewSet(viewsets.ViewSet):
    serializer_class = PessoaSerializer

    def list(self, request):
        # Pegando os parâmetros de consulta
        nome = request.query_params.get("nome", None)
        data_nasc = request.query_params.get("data_nasc", None)
        cpf = request.query_params.get("cpf", None)
        sexo = request.query_params.get("sexo", None)
        altura = request.query_params.get("altura", None)
        peso = request.query_params.get("peso", None)

        # Iniciando a consulta básica
        queryset = Pessoa.objects.all()

        # Aplicando os filtros conforme os parâmetros recebidos
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        if data_nasc:
            queryset = queryset.filter(data_nasc=data_nasc)
        if cpf:
            queryset = queryset.filter(cpf=cpf)
        if sexo:
            queryset = queryset.filter(sexo=sexo)
        if altura:
            queryset = queryset.filter(altura=altura)
        if peso:
            queryset = queryset.filter(peso=peso)

        # Serializando os resultados
        serializer = PessoaSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        cpf = request.data.get("cpf")

        # Verificando se o CPF já existe
        if Pessoa.objects.filter(cpf=cpf).exists():
            return Response(
                {"error": "CPF já cadastrado!"}, status=status.HTTP_400_BAD_REQUEST
            )
        pessoa = criar_pessoa(request.data)
        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        pessoa = obter_pessoa_por_id(pk)
        if pessoa:
            serializer = PessoaSerializer(pessoa)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        pessoa = obter_pessoa_por_id(pk)
        if pessoa:
            pessoa = atualizar_pessoa(pessoa, request.data)
            serializer = PessoaSerializer(pessoa)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        pessoa = obter_pessoa_por_id(pk)
        if pessoa:
            excluir_pessoa(pessoa)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=["get"])
    def peso_ideal(self, request, pk=None):
        pessoa = obter_pessoa_por_id(pk)
        if pessoa:
            return Response({"peso_ideal": calcular_peso_ideal(pessoa)})
        return Response(status=status.HTTP_404_NOT_FOUND)
