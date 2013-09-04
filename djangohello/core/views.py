# coding: utf-8
from django.shortcuts import render

class Pessoa:
    nome = ""
    def __init__(self, nome):
        self.nome = nome

def home(request):
    # regras...
    p = Pessoa('Fabiano')
    p2 = Pessoa('Fulano')
    p3 = Pessoa('Outro')
    
    lista = list()
    lista.append(p)
    lista.append(p2)
    lista.append(p3)
    return render(request, 'index.html', {'titulo': 'Django Hello World!!!', 
                                          'pessoa': p, 
                                          'lista': lista,})

