# main/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import (
    buscar_produtos_disponiveis,
    buscar_produtos_agricultor,
    cadastrar_produto,
    deletar_produto,
    exemplo_dados,
    register_user,
    login_user,
    logout_user
)

urlpatterns = [
    path('produtos/disponiveis/', buscar_produtos_disponiveis, name='buscar_produtos_disponiveis'),
    path('produtos/agricultor/<int:id_agricultor>/', buscar_produtos_agricultor, name='buscar_produtos_agricultor'),
    path('produtos/cadastrar/', cadastrar_produto, name='cadastrar_produto'),
    path('produtos/deletar/<int:id_produto>/<int:id_agricultor>/', deletar_produto, name='deletar_produto'),
    path('api/exemplo/', exemplo_dados, name='exemplo_dados'),
    path('auth/register/', register_user, name='register'),
    path('auth/login/', login_user, name='login'),
    path('auth/logout/', logout_user, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)