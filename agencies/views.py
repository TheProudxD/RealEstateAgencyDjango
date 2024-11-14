from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Agent

menu = ["О сайте", "Студенты", "Преподаватели", "Войти"]


def index(request):
    agents = Agent.objects.all()
    return render(request, 'agents/index.html', {'agents': agents, 'menu': menu, 'title':
        'Главная страница'})


def groups(request, group):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Список иноагентов: </h1> <div style='color: rgb(94, 25, 10);'>{group}</div")


def about(request):
    return render(request, 'agents/about.html', {'menu': menu, 'title': ' О сайте'})
