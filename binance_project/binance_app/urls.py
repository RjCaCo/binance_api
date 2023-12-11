from django.urls import path
from .views import index, obter_dados_da_api

urlpatterns = [
    path('', index, name='index'),
    path('obter_dados_da_api/', obter_dados_da_api, name='obter_dados_da_api'),
]