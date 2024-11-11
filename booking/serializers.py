from rest_framework import serializers
from users.models import User
from courses.models import Unit
from tutor_availability.models import TutorAvailability
from booking.models import Booking

class BookingSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True, required=False
    )
    unit = serializers.PrimaryKeyRelatedField(
        queryset=Unit.objects.all(), write_only=True, required=False, many=True
    )
    tutor_availability = serializers.PrimaryKeyRelatedField(
        queryset=TutorAvailability.objects.all(), write_only=True, required=False
    )
    student_details = serializers.SerializerMethodField(read_only=True) 
    unit_details = serializers.SerializerMethodField(read_only=True) 
    tutor_availability_details = serializers.SerializerMethodField(read_only=True) 

    class Meta:
        model = Booking
        fields = ['id', 'student','tutor_availability', 'unit', 
                  'requested_date', 'status', 'student_details', 
                  'unit_details', 'tutor_availability_details']
        
    def get_student_details(self, obj):
        if obj.student:
            return {
                "first_name": obj.student.first_name,
                "last_name": obj.student.last_name
            }
        return None
    
    def get_unit_details(self, obj):
        # Loop over units since it's now a ManyToMany relationship
        return [
            {
                "id": unit.id,
                "unit_name": unit.unit_name,
                "unit_description": unit.description
            } for unit in obj.unit.all()
        ]
    
    def get_tutor_availability_details(self, obj):
        if obj.tutor_availability:
            return {
                "first_name": obj.tutor_availability.tutor.first_name,
                "last_name": obj.tutor_availability.tutor.last_name,
                'day_of_week': obj.tutor_availability.day_of_week,
                'hourly_rate': obj.tutor_availability.hourly_rate
            }
        return None
        
    def validate_tutor(self, student):
        if  student.is_tutor==True:
            raise serializers.ValidationError("The selected user is not a student.")
        return student