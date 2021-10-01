from django.db.models import Q
from django.shortcuts import render, Http404, get_object_or_404
from django.contrib import messages
from .models import Games

def index(request):
    dados = Games.objects.order_by('-id').filter(
        mostrar=True
    )
    return render(request,'home/index.html',{'dados':dados})

def mostrar(request, idbusca):
    dados = get_object_or_404(Games,id=idbusca)
    return render(request, 'home/detailGame.html',{'dados':dados})

def buscar(request):
    x = request.GET['buscar']
    if x is None or not x:
        messages.add_message(request,messages.INFO,'Digite um valor válido')
        return render(request,'home/index.html')

    dados = Games.objects.order_by('title').filter(
        Q(title__icontains=x) | Q(description__icontains=x)
    )
    return render(request,'home/index.html',{'dados':dados})
