from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, PessoaViewSet

router = DefaultRouter()
router.register(r"pessoas", PessoaViewSet, basename="pessoa")

urlpatterns = [
    path("", index, name="index"),
    path("api/", include(router.urls)),
]
