from rest_framework import viewsets
from rest_framework_simple_api_key.permissions import IsActiveEntity

from organization.backend import OrganizationAPIKeyAuthentication
from payment.models import Payment
from payment.serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post"]
    authentication_classes = (OrganizationAPIKeyAuthentication,) # ensures every request on this endpoint requires a valid API key
    permission_classes = (IsActiveEntity,)
    serializer_class = PaymentSerializer
    
    def get_queryset(self):
        return Payment.objects.filter(organization=self.request.user)
