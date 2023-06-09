from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('realizar_consumo/', views.realizar_consumo, name='realizar_consumo'),
    path('recarregar_comanda/<int:id>', views.recarregar_comanda, name='recarregar_comanda'),
    path('detalhes/<int:id>', views.detalhes, name='detalhes'),
    path('pesquisar_comanda/', views.pesquisar_comanda, name='pesquisar_comanda'),
    path('ferramentas/', views.ferramentas, name='ferramentas'),
    path('sobre/', views.sobre, name='sobre'),
    path('busca_id/', views.search, name='busca_id')
]