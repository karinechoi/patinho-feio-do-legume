from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Produto
from ..serializers import ProdutoSerializer

@api_view(['GET'])
def buscar_produtos_agricultor(request, id_agricultor):
    produtos = Produto.objects.filter(id_agricultor=id_agricultor)
    serializer = ProdutoSerializer(produtos, many=True)
    return Response(serializer.data)
