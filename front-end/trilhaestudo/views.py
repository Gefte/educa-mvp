from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'trilhaestudo/index.html')

def imagem(request):
    return render(request,'trilhaestudo/imagem.html')
    