# main/tests/test_buscar_produtos_disponiveis.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from main.models import Produto

class BuscarProdutosDisponiveisTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Criando produtos com e sem quantidade
        Produto.objects.create(nome="Produto 1", quantidade=10, id_agricultor=1)
        Produto.objects.create(nome="Produto 2", quantidade=0, id_agricultor=1)

    def test_buscar_produtos_disponiveis(self):
        url = reverse('buscar_produtos_disponiveis')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Apenas um produto disponível
        self.assertEqual(response.data[0]['nome'], "Produto 1")
