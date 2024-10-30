from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Produto
from main.serializers import ProdutoSerializer

@api_view(['GET'])
def buscar_produtos_disponiveis(request):
    produtos = Produto.objects.filter(quantidade__gt=0)  # Produtos com quantidade > 0 (disponíveis)
    serializer = ProdutoSerializer(produtos, many=True)
    return Response(serializer.data)
