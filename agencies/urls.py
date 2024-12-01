from django.urls import path
from .views import AgentHome, ShowAgent, AddAgent, agents, about, clients, login, show_client, show_agent, addagent

urlpatterns = [
path('', AgentHome.as_view(), name='home'),
path('about/', about, name='about'),
path('agents', agents, name='agents'),
path('clients/', clients, name='clients'),
path('login/', login, name='login'),
path('client/<int:cl_id>/', show_client, name='client'),
path('agent/<slug:ag_slug>/', ShowAgent.as_view(), name='agent'),
path('addagent/', AddAgent.as_view(), name='addagent'),
]