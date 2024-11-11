from django.urls import path
from .views import index, groups
urlpatterns = [ 
    path('', index), 
    path('groups/<slug:group>/', groups), ]
    