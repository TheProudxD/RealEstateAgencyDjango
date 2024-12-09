from django_filters import FilterSet, DateFilter, CharFilter 
from .models import Agent 

class AgentFilter(FilterSet): 
    #start_date = DateFilter(field_name='birth_date', lookup_expr='gte') 
    name = CharFilter(field_name='name', lookup_expr='contains', label='Имя') 
    
    class Meta:
        model = Agent 
        fields = ['name', 'agreement']