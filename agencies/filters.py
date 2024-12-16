import django_filters
from .models import Agent

class AgentFilter(django_filters.FilterSet):    
    # price = NumberFilter(field_name='price', lookup_expr='lte', label='Цена') 
    # agreement = BooleanFilter(field_name='agreement', lookup_expr='exact', label='Договор') 
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label='',
        widget=django_filters.widgets.forms.TextInput(attrs={
            'placeholder': 'Поиск по имени или специализации...',
            'class': 'search-input'
        })
    )
    
    price = django_filters.CharFilter(
        field_name='agreement__price',
        lookup_expr='lte',
        label='',
        widget=django_filters.widgets.forms.TextInput(attrs={
            'placeholder': 'Поиск по стоимости...',
            'class': 'search-input'
        })
    )

    class Meta:
        model = Agent
        fields = ['name', 'price']