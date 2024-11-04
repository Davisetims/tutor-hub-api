from rest_framework import serializers
from booking.models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        
    def validate_tutor(self, student):
        if  student.is_tutor==True:
            raise serializers.ValidationError("The selected user is not a student.")
        return student