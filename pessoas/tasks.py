def calcular_peso_ideal(pessoa):
    return pessoa.calcular_peso_ideal()


# backend/pessoas/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Pessoa
from .serializers import PessoaSerializer
from .services import (
    criar_pessoa,
    atualizar_pessoa,
    excluir_pessoa,
    listar_pessoas,
    obter_pessoa_por_id,
)
from .tasks import calcular_peso_ideal


class PessoaViewSet(viewsets.ViewSet):
    def list(self, request):
        pessoas = listar_pessoas()
        serializer = PessoaSerializer(pessoas, many=True)
        return Response(serializer.data)

    def create(self, request):
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
