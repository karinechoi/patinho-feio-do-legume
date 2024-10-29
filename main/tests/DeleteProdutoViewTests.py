# main/tests/test_deletar_produto.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from main.models import Produto

class DeletarProdutoTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Criando um produto para o agricultor 1
        self.produto = Produto.objects.create(nome="Produto Teste", quantidade=10, id_agricultor=1)

    def test_deletar_produto_com_sucesso(self):
        url = reverse('deletar_produto', args=[self.produto.id_produto, 1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Produto.objects.count(), 0)  # Produto deve ter sido deletado

    def test_deletar_produto_sem_permissao(self):
        url = reverse('deletar_produto', args=[self.produto.id_produto, 2])  # id_agricultor diferente
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Produto.objects.count(), 1)  # Produto não deve ser deletado
