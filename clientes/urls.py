from django.urls import path, include
from . import views


urlpatterns = [
    # path("", views.index, name="home"),
    path("cadastrar_cliente/", views.cadastrar_cliente, name="cadastrar_cliente"),
    
]