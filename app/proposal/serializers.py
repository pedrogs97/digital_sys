from rest_framework import serializers
from proposal.models import Proposal, Address


class AddressSerialzier(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Address


class ProposalSerialzier(serializers.ModelSerializer):
    address = AddressSerialzier(many=True, read_only=False)

    class Meta:
        fields = "__all__"
        model = Proposal


class NewProposalSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=150, required=True, write_only=True)
    taxpayer_identification = serializers.CharField(max_length=17, required=True, write_only=True)
    loan_value = serializers.DecimalField(max_digits=12, decimal_places=2, required=True, write_only=True)
    country = serializers.CharField(max_length=50, required=True, write_only=True)
    state = serializers.CharField(max_length=50, required=True, write_only=True)
    city = serializers.CharField(max_length=50, required=True, write_only=True)
    street = serializers.CharField(max_length=250, required=True, write_only=True)
    number = serializers.IntegerField(required=True, write_only=True)
    complement = serializers.CharField(max_length=100, required=True, write_only=True)
    zip_code = serializers.CharField(max_length=8, required=True, write_only=True)

    def create(self, validated_data):
        proposal = Proposal.objects.create(
            full_name=validated_data["full_name"],
            taxpayer_identification=validated_data["taxpayer_identification"],
            loan_value=validated_data["loan_value"],
        )
        Address.objects.create(
            country=validated_data["country"],
            state=validated_data["state"],
            city=validated_data["city"],
            street=validated_data["street"],
            number=validated_data["number"],
            complement=validated_data["complement"],
            zip_code=validated_data["zip_code"],
            proposal=proposal,
        )
        return proposal
    
    def update(self, instance, validated_data):
        raise NotImplementedError('Not implemented.')
    
    def to_representation(self, instance):
        return ProposalSerialzier(instance).data