from .models import Pessoa


def criar_pessoa(dados):
    return Pessoa.objects.create(**dados)


def atualizar_pessoa(pessoa, dados):
    for key, value in dados.items():
        setattr(pessoa, key, value)
    pessoa.save()
    return pessoa


def excluir_pessoa(pessoa):
    pessoa.delete()


def listar_pessoas():
    return Pessoa.objects.all()


def obter_pessoa_por_id(pessoa_id):
    return Pessoa.objects.filter(id=pessoa_id).first()
