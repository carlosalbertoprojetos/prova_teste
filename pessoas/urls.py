from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PessoaViewSet, index, listar_pessoas, criar_pessoa

router = DefaultRouter()
router.register(r"pessoas", PessoaViewSet, basename="pessoa")

urlpatterns = [
    # path("", include(router.urls)),
    path("", index, name="index"),
    path("pessoas/", listar_pessoas, name="listar_pessoas"),
    path("api/pessoas/", criar_pessoa, name="criar_pessoa"),
]
