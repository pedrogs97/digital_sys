from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from proposal.models import Proposal
from proposal.serializers import ProposalSerialzier, NewProposalSerializer
from proposal.tasks import analyze_proposal



class ProposalModelViewSet(ModelViewSet):
    authentication_classes = None
    permission_classes = AllowAny
    serializer_class = ProposalSerialzier
    queryset = Proposal.objects.all()
    http_method_names = ["get", "put", "patch"]

    @action(detail=False, methods=["POST"])
    def new_proposal(self, request, *args, **kwargs):
        serializer = NewProposalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        analyze_proposal.delay(instance.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
