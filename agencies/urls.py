from django.urls import path
from .views import index, agents, about, clients, login, show_client, show_agent

urlpatterns = [
path('', index, name='home'),
path('about/', about, name='about'),
path('agents', agents, name='agents'),
path('clients/', clients, name='clients'),
path('login/', login, name='login'),
path('client/<int:cl_id>/', show_client, name='client'),
path('agent/<slug:ag_slug>/', show_agent, name='agent'),
]