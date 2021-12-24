from django.urls import path
from Ativo import views

app_name = "ativos"

urlpatterns = [    
    path('listar_ativos/', views.listar_ativos, name='listar_ativos'),
    path('detalhes_ativo/<int:pk>', views.detalhes_ativo, name='detalhes_ativo'),
]
