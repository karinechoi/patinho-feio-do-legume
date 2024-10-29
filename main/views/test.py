# main/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def exemplo_dados(request):
    data = {
        "mensagem": "Olá do Django!",
        "dados": [1, 2, 3, 4, 5]
    }
    return Response(data)
