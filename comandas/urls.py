from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('recarregar_comanda/', views.recarregar_comanda, name='recarregar_comanda'),
    path('realizar_consumo/', views.realizar_consumo, name='realizar_consumo'),
    path('ferramentas/', views.ferramentas, name='ferramentas'),
    path('sobre/', views.sobre, name='sobre')
]