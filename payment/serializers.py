from rest_framework import serializers
from payment.models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    user= serializers.SerializerMethodField()
    class Meta:
        model = Payment
        fields = '__all__'
    
    def get_user(self,obj):
        if obj.user:
            return {
                'first_name': obj.user.first_name,
                'last_name': obj.user.last_name,
                'email': obj.user.email
            }
        return None
    
   
        