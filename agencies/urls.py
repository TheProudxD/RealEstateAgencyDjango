from django.urls import path
from django.views.generic import RedirectView
from .views import AgentHome, ShowAgent, AddAgent, agents, about, clients, login, show_client, show_agent, addagent

urlpatterns = [
path('', AgentHome.as_view(), name='home'),
path('favicon.ico', RedirectView.as_view(url='/static/agents/images/favicon.ico')),
path('about/', about, name='about'),
path('agents', agents, name='agents'),
path('clients/', clients, name='clients'),
path('login/', login, name='login'),
path('client/<int:cl_id>/', show_client, name='client'),
path('agent/<slug:ag_slug>/', ShowAgent.as_view(), name='agent'),
path('addagent/', AddAgent.as_view(), name='addagent'),
]