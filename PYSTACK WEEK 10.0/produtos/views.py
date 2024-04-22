from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto

def cadastrar(request):
    if request.method == "GET":
        cd_erro = request.GET.get('cd_erro')
        texto = request.GET.get('texto')
        
        return render(request, 'index.html', {'cd_erro': cd_erro, 'texto': texto })
    elif request.method == "POST":
        produto = request.POST.get('produto')
        preco = request.POST.get('preco')

        if len(produto) <= 0:
            return redirect('/produtos/cadastrar/?cd_erro=1&texto=Digite o nome completo do produt')
        
        produto = Produto(
            nome_produto = produto,
            preco = preco
        )

        produto.save()
        
        return HttpResponse('Fui chamado')