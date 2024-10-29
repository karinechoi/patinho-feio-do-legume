from rest_framework import serializers
from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id_produto', 'nome', 'descricao', 'foto', 'quantidade', 'id_agricultor', 'classificacao', 'tipo_produto', 'tipo_medida']