from .models import Agent, Agreement
from .serializers import AgentSerializer, AgentDetailSerializer
from rest_framework.response import Response 
from rest_framework.views import APIView
from django.forms import model_to_dict
from rest_framework import viewsets
from rest_framework.decorators import action 
from .utils import AgentAPIPagination
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly, UserPermission
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class AgentViewSet(viewsets.ModelViewSet):
    pagination_class = AgentAPIPagination
    permission_classes = [UserPermission]

    @action(methods=['get'], detail=True)
    def agreement(self, request, pk=None):
        group = Agreement.objects.filter(pk=pk).first()
        if group:
            return Response({'agreement': f'{group.id}-{group.price}'})
        else:
            return Response({'agreement': 'Группа не найдена'})
        
    def get_queryset(self):
        agreement = self.request.GET.get('agreement', '')
        if agreement:
            return Agent.objects.filter(agreement_id=agreement)
        else:
            return Agent.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AgentDetailSerializer
        return AgentSerializer
    
class AgreementAPIView(APIView): 
    def get(self, request): 
        ag = Agreement.objects.all().values()
        return Response({'agreements': list(ag)}) 
    def post(self, request): 
        new_ag = Agreement.objects.create(price=request.data['price']) 
        return Response({'agreement': model_to_dict(new_ag)})