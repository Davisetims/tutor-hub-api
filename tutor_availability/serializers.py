from rest_framework import serializers
from tutor_availability.models import TutorAvailability


class TutorAvailabilitySerializer(serializers.ModelSerializer):
    tutor = serializers.SerializerMethodField()
    class Meta:
        model = TutorAvailability
        fields = ['tutor', 'day_of_week', 'hourly_rate']
        
    
    def get_tutor(self, obj):
        if obj.tutor:
            return {
                "first name": obj.tutor.first_name,
                "last name": obj.tutor.last_name
            }
        return None
    
    def validate_tutor(self, tutor):
        if not tutor.is_tutor:
            raise serializers.ValidationError("The selected user is not a tutor.")
        return tutor

