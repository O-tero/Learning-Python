from rest_framework import serializers

from organization.models import Organization
from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(
        queryset = Organization.objects.all()
    )
    
    class Meta:
        model = Payment
        fields = "__all__"
