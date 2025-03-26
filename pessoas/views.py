import json
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
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


def index(request):
    return render(request, "pessoas/cadastro_pessoa.html")


@csrf_exempt  # Se você estiver usando AJAX sem CSRF (ou adicionar manualmente o CSRF token)
@require_http_methods(["POST"])
def criar_pessoa(request):
    try:
        # Parse da requisição JSON
        data = json.loads(request.body)

        # Criação do objeto Pessoa
        pessoa = Pessoa.objects.create(
            nome=data.get("nome"),
            data_nasc=data.get("data_nasc"),
            cpf=data.get("cpf"),
            sexo=data.get("sexo"),
            altura=data.get("altura"),
            peso=data.get("peso"),
        )

        # Retorno de sucesso com dados da pessoa
        return JsonResponse({"id": pessoa.id, "nome": pessoa.nome}, status=201)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


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
