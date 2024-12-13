from rest_framework import serializers
from .models import Agent

class AgentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    credit = serializers.CharField(max_length=50)

    class Meta:
        model = Agent
        fields = ('name', 'credit', "agreement", "slug")

class AgentModel:
    def __init__(self, name, credit):
        self.name = name
        self.credit = credit

class AgentDetailSerializer(serializers.ModelSerializer): 
    group_name = serializers.SerializerMethodField() 

    class Meta:
        model = Agent 
        fields = '__all__' 
    def get_group_name(self, obj): 
        return f'{obj.agreement.id}-{obj.agreement.price}'