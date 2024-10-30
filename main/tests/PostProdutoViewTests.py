# main/tests/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from main.models import Produto

class ProdutoTests(APITestCase):
    
    def test_cadastrar_produto(self):
        # Define a URL do endpoint para cadastro de produto
        url = reverse('cadastrar_produto')
        
        # Dados que serão enviados para criar um novo produto
        data = {
            "nome": "Banana",
            "descricao": "Banana orgânica fresca",
            "foto": "/home/aline/Documents/faculdade/lab engenharia/backend-django/produto-webserver/static/nome.png",
            "quantidade": "20.00",
            "id_agricultor": 3,
            "classificacao": "4.8",
            "tipo_produto": "Fruta",
            "tipo_medida": "kg"
        }
        
        # Faz a requisição POST para o endpoint com os dados
        response = self.client.post(url, data, format='json')
        
        # Verifica se o status da resposta é 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Verifica se o produto foi criado corretamente no banco de dados
        self.assertEqual(Produto.objects.count(), 1)
        produto = Produto.objects.get()
        self.assertEqual(produto.nome, "Banana")
        self.assertEqual(produto.quantidade, 20.00)

    def test_cadastrar_produto_invalido(self):
        # Define a URL do endpoint para cadastro de produto
        url = reverse('cadastrar_produto')
        
        # Dados inválidos (por exemplo, sem o campo obrigatório 'nome')
        data = {
            "descricao": "Produto sem nome",
            "quantidade": "15.00",
            "id_agricultor": 3,
            "classificacao": "4.5",
            "tipo_produto": "Outro",
            "tipo_medida": "kg"
        }
        
        # Faz a requisição POST para o endpoint com dados inválidos
        response = self.client.post(url, data, format='json')
        
        # Verifica se o status da resposta é 400 (Bad Request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Verifica que o produto não foi criado no banco de dados
        self.assertEqual(Produto.objects.count(), 0)
