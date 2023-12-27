from django.urls import path
from .views import index, atualizado, inicial, solanaInicial, solanaAtualizado

urlpatterns = [
    path('', index, name='index'),
    path('inicial/', inicial, name='inicial'),
    path('atualizado/', atualizado, name='atualizado'),
    path('solanaInicial/', solanaInicial, name='solanaInicial'),
    path('solanaAtualizado/', solanaAtualizado, name='solanaAtualizado'),
]