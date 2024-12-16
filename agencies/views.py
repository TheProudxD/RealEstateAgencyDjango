from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from agencies.filters import AgentFilter
from .forms import AddAgentForm, FilterAgentForm, RegisterUserForm, LoginUserForm, ContactForm
from .models import Agent, Client
from .utils import menu, DataMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class AgentsView(DataMixin, ListView):
    model = Agent
    template_name = 'agents/agents_list.html'
    context_object_name = 'agents'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        auth = self.request.user.is_authenticated
        queryset = self.get_queryset()
        ag_filter = AgentFilter(self.request.GET, queryset)
        c_def = self.get_user_context(title='Наши агенты', auth=auth, ag_filter=ag_filter)
        return {**context, **c_def}
    
    def get_queryset(self):
        queryset = super().get_queryset()
        ag_filter = AgentFilter(self.request.GET, queryset)
        return ag_filter.qs
        
        
    # def get_queryset(self):
    #    return Agent.objects.filter()
class AgentHome(DataMixin, ListView):
    model = Agent
    template_name = 'agents/index.html'
    context_object_name = 'agents'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        auth = self.request.user.is_authenticated
        queryset = self.get_queryset()
        ag_filter = AgentFilter(self.request.GET, queryset)
        contact_form = ContactForm()
        c_def = self.get_user_context(
            title='Главная страница', 
            auth=auth, 
            ag_filter=ag_filter,
            contact_form=contact_form
        )
        return {**context, **c_def}
    
    def get_queryset(self):
        queryset = super().get_queryset()
        ag_filter = AgentFilter(self.request.GET, queryset)
        return ag_filter.qs
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сообщение успешно отправлено!')
            return redirect('home')
        return self.get(request, *args, **kwargs)
    


class ShowAgent(DataMixin, DetailView):
    model = Agent
    template_name = 'agents/agent.html'
    slug_url_kwarg = 'ag_slug'
    context_object_name = 'ag'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context, **c_def}

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сообщение успешно отправлено!')
            return redirect('agents')
        else:
            messages.error(request, 'Ошибка при отправке сообщения')
            return self.get(request, *args, **kwargs)


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

    def form_valid(self, form):
        response = super().form_valid(form)
        # После успешной аутентификации перенаправляем на главную
        return response
