from django.shortcuts import render



def index(request):
    dados ={
    1: {"Nome":"Matemática",
        "legenda":"Explorando as Maravilhas da Matemática 🧮🚀 ",
        "card":"Matemática"},
    2: {"Nome": "Física",
        "legenda":"Trilhando o Caminho do Conhecimento em Física ⚛️🌌 ",
        "card":"Física"}
    }
    return render(request, 'trilhaestudo/index.html',{"cards":dados})

def imagem(request):
    return render(request,'trilhaestudo/imagem.html')
    