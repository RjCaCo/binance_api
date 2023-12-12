from django.urls import path
from .views import index, atualizado, inicial

urlpatterns = [
    path('', index, name='index'),
    path('inicial/', inicial, name='inicial'),
    path('atualizado/', atualizado, name='atualizado'),
]