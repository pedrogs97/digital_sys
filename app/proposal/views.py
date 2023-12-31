from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from proposal.models import Proposal
from proposal.serializers import ProposalSerialzier
from proposal.tasks import analyze_proposal



class ProposalModelViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    serializer_class = ProposalSerialzier
    queryset = Proposal.objects.all()

    def create(self, request, *args, **kargs): 
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        analyze_proposal.delay(instance.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
