# main/tests/test_buscar_produtos_agricultor.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from main.models import Produto

class BuscarProdutosAgricultorTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Criando produtos para dois agricultores
        Produto.objects.create(nome="Produto 1", quantidade=10, id_agricultor=1)
        Produto.objects.create(nome="Produto 2", quantidade=20, id_agricultor=2)

    def test_buscar_produtos_agricultor(self):
        url = reverse('buscar_produtos_agricultor', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Apenas um produto do agricultor 1
        self.assertEqual(response.data[0]['id_agricultor'], 1)
