from django.shortcuts import render
from rest_framework import viewsets, permissions
from payment.models import Payment
from payment.serializers import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            payment = Payment.objects.filter(user=user)
        else:
            payment = Payment.objects.all()
        return payment
