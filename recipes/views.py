from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contato(request):
    return HttpResponse('<h1>Contato!!</h1>')


def sobre(request):
    return HttpResponse('<h1>Sobre</h1>')

