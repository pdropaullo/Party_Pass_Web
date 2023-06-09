from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_produtos/', views.cadastrar_produtos, name='cadastrar_produtos'),
    path('pesquisar_produtos/', views.pesquisar_produtos, name='pesquisar_produtos'),
    path('detalhes/<int:id>', views.detalhes, name='detalhes'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('busca/', views.search, name='busca')
] 
