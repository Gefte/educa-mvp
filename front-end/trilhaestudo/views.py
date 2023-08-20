from django.shortcuts import render
from trilhaestudo.models import Materia



def index(request):
    materia = Materia.objects.all()
   
    return render(request, 'trilhaestudo/index.html',{"cards":materia})

def imagem(request):
    return render(request,'trilhaestudo/imagem.html')
    