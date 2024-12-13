from django.urls import include, path
from django.views.generic import RedirectView
from rest_framework import routers
from agencies.viewsets import AgentViewSet, AgreementAPIView
from .views import AgentHome, ShowAgent, AddAgent, agents, about, clients, show_client, show_agent, addagent, \
    RegisterUser, LoginUser, logout_user

router = routers.DefaultRouter()
router.register(r'agents', AgentViewSet, basename='agents')
urlpatterns = [
path('', AgentHome.as_view(), name='home'),
path('favicon.ico', RedirectView.as_view(url='/static/agents/images/favicon.ico')),
path('about/', about, name='about'),
path('agents', agents, name='agents'),
path('login/', LoginUser.as_view(), name='login'),
path('clients/', clients, name='clients'),
path('client/<int:cl_id>/', show_client, name='client'),
path('agent/<slug:ag_slug>/', ShowAgent.as_view(), name='agent'),
path('addagent/', AddAgent.as_view(), name='addagent'),
path('register/', RegisterUser.as_view(), name='register'),
path('logout/', logout_user, name='logout'),
path('api/v1/agreements/', AgreementAPIView.as_view()),
#path('api/v1/agents/', AgentAPIView.as_view()),
#path('api/v1/agent/<int:pk>/', AgentAPIDetailView.as_view()),
#path('api/v1/agents/', AgentViewSet.as_view({'get': 'list'})), 
#path('api/v1/agent/<int:pk>/', AgentViewSet.as_view({'put': 'update'})),
path('api/v1/', include(router.urls)),
]