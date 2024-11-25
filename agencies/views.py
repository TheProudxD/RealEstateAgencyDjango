from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from agencies.forms import AddAgentForm
from .models import Agent, Client

menu = [{'title': "О сайте", 'url_name': 'about'},
{'title': "Клиенты", 'url_name': 'clients'},
{'title': "Агенты", 'url_name': 'agents'},
{'title': "Войти", 'url_name': 'login'}]

class AgentHome(ListView):
    model = Agent 
    template_name = 'agents/index.html'
    context_object_name = 'agents'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['menu'] = menu
        return context
    
    #def get_queryset(self): 
    #    return Agent.objects.filter()

class ShowAgent(DetailView): 
    model = Agent 
    template_name = 'agents/agent.html' 
    slug_url_kwarg = 'ag_slug' 
    context_object_name = 'ag'

class AddStudent(CreateView): 
    form_class = AddAgentForm
    template_name = 'agents/addagent.html'
    success_url = reverse_lazy('home')

def index(request):
    agents = Agent.objects.all()
    context = {
    'agents': agents,
    'menu': menu,
    'title': 'Главная страница'
    }
    return render(request, 'agents/index.html', context=context)


def agents(request):
    if request.GET:
        print(request.GET)
    return HttpResponse("Агенты")
    #return HttpResponse(f"<h1>Список агентов: </h1> <div style='color: rgb(94, 25, 10);'>{32}</div")

def about(request):
    return render(request, 'agents/about.html', {'menu': menu, 'title': 'О сайте'})

def clients(request):
    return HttpResponse("Клиенты")

def login(request):
    return HttpResponse("Авторизация")

def show_client(request, cl_id):
    return HttpResponse(f"Отображение клиента с id = {cl_id}")

def show_agent(request, ag_slug):
    agent = get_object_or_404(Agent, slug=ag_slug) 
    context = { 'ag': agent, 'menu': menu, } 
    return render(request, 'agents/agent.html', context=context)

def addagent(request):
    if request.method=="POST":
        form = AddAgentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка!')
    else:
        form = AddAgentForm()
    return render(request, 'agents/addagent.html', {'form':form})