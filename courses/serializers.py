from courses.models import Course, Unit
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields  = '__all__'