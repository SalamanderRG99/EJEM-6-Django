from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("alunos/", views.lista, name="lista"),
    path("alunos/<str:slug>/", views.detalhe, name="detalhe"),
]