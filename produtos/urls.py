from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_produtos/', views.cadastrar_produtos, name='cadastrar_produtos')
]