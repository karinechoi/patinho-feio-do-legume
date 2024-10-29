from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Produto

@api_view(['DELETE'])
def deletar_produto( id_produto, id_agricultor):
    try:
        # Tenta encontrar o produto pelo id
        produto = Produto.objects.get(id_produto=id_produto)

        # Verifica se o id_agricultor corresponde ao do produto
        if produto.id_agricultor != id_agricultor:
            return Response(
                {"detail": "Você não tem permissão para deletar este produto."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Se o id_agricultor for o mesmo, permite a exclusão
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    except Produto.DoesNotExist:
        return Response(
            {"detail": "Produto não encontrado."},
            status=status.HTTP_404_NOT_FOUND
        )