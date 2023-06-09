from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('recarregar_comanda/<int:id>', views.recarregar_comanda, name='recarregar_comanda'),
    path('detalhes_comanda/<int:id>', views.detalhes_comanda, name='detalhes_comanda'),
    path('pesquisar_comanda/', views.pesquisar_comanda, name='pesquisar_comanda'),
    path('ferramentas/', views.ferramentas, name='ferramentas'),
    path('sobre/', views.sobre, name='sobre'),
    path('busca_id/', views.search, name='busca_id'),
    path('search_id_consumo/', views.search_id_consumo, name='search_id_consumo'),
    path('pesquisar_comanda_consumo/', views.pesquisar_comanda_consumo, name='pesquisar_comanda_consumo'),
    path('realizar_consumo/<int:id>', views.realizar_consumo, name='realizar_consumo'),
]