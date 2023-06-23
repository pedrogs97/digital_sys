from rest_framework import serializers
from proposal.models import Proposal, Address


class AddressSerialzier(serializers.ModelSerializer):

    class Meta:
        exclude = ['proposal']
        model = Address


class ProposalSerialzier(serializers.ModelSerializer):
    address = AddressSerialzier(many=True)

    class Meta:
        fields = "__all__"
        model = Proposal

    def create(self, validated_data):
        addresses = validated_data.pop('address')
        proposal = Proposal.objects.create(**validated_data)
        for address in addresses:
            Address.objects.create(proposal=proposal, **address)
        return proposal
