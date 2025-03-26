from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PessoaViewSet, index

router = DefaultRouter()
router.register(r"pessoas", PessoaViewSet, basename="pessoa")

urlpatterns = [
    path("", index, name="index"),
    # path("", include(router.urls))
]
