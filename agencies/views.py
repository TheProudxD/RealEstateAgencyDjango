from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import AddAgentForm, RegisterUserForm, LoginUserForm
from .models import Agent, Client
from .utils import menu, DataMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class AgentHome(DataMixin, ListView):
    model = Agent
    template_name = 'agents/index.html'
    context_object_name = 'agents'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        auth = self.request.user.is_authenticated
        c_def = self.get_user_context(title='Главная страница', auth=auth)
        return {**context, **c_def}

    # def get_queryset(self):
    #    return Agent.objects.filter()


class ShowAgent(DataMixin, DetailView):
    model = Agent
    template_name = 'agents/agent.html'
    slug_url_kwarg = 'ag_slug'
    context_object_name = 'ag'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context, **c_def}


class AddAgent(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('home')
    raise_exception = True
    form_class = AddAgentForm
    template_name = 'agents/addagent.html'
    success_url = reverse_lazy('home')


def agents(request):
    if request.GET:
        print(request.GET)
    return HttpResponse("Агенты")
    # return HttpResponse(f"<h1>Список агентов: </h1> <div style='color: rgb(94, 25, 10);'>{32}</div")


def about(request):
    return render(request, 'agents/about.html', {'menu': menu, 'title': 'О сайте'})


def clients(request):
    return HttpResponse("Клиенты")


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'agents/register.html'
    success_url = reverse_lazy('show_client')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return {**context, **c_def}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

def show_client(request, cl_id):
    return HttpResponse(f"Отображение клиента с id = {cl_id}")


def show_agent(request, ag_slug):
    agent = get_object_or_404(Agent, slug=ag_slug)
    context = {'ag': agent, 'menu': menu, }
    return render(request, 'agents/agent.html', context=context)


def addagent(request):
    if request.method == "POST":
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
    return render(request, 'agents/addagent.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'agents/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return {**context, **c_def}

    def get_success_url(self):
        return reverse_lazy('home')
