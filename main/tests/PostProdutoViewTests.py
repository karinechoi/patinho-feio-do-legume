# main/tests/test_cadastrar_produto.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from main.models import Produto

class CadastrarProdutoTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_cadastrar_produto(self):
        url = reverse('cadastrar_produto')
        data = {
            "nome": "Produto Teste",
            "descricao": "Descrição do produto teste",
            "quantidade": 15,
            "id_agricultor": 1,
            "classificacao": 4.5,
            "tipo_produto": "Legume",
            "tipo_medida": "kg"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Produto.objects.count(), 1)
        self.assertEqual(Produto.objects.get().nome, "Produto Teste")
