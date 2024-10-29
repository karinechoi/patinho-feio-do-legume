# main/urls.py
from django.urls import path
from main.views import (
    buscar_produtos_disponiveis,
    buscar_produtos_agricultor,
    cadastrar_produto,
    deletar_produto, 
    test
)

urlpatterns = [
    path('produtos/disponiveis/', buscar_produtos_disponiveis, name='buscar_produtos_disponiveis'),
    path('produtos/agricultor/<int:id_agricultor>/', buscar_produtos_agricultor, name='buscar_produtos_agricultor'),
    path('produtos/cadastrar/', cadastrar_produto, name='cadastrar_produto'),
    path('produtos/deletar/<int:id_produto>/<int:id_agricultor>/', deletar_produto, name='deletar_produto'),
    path('api/exemplo/', test, name='exemplo_dados'),
]
