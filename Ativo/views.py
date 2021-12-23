from django.shortcuts import render
from Ativo.models import Ativo

def listar_ativos(request):
   lista_ativos = Ativo.objects.all()
   informacoes = {
       'ativos': lista_ativos
   }
   return render(request, 'ativos/listar_ativos.html', informacoes) 

def detalhes_ativo(request, pk):
    ativo = Ativo.objects.filter(id=pk)[0]
    
    informacoes = {
        'detalhes_ativo':ativo
    }
    
    return render(request, 'ativo/detalhes_ativo.html', informacoes)