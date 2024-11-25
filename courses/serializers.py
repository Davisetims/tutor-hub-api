from courses.models import Course, Unit
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
class UnitSerializer(serializers.ModelSerializer):
    tutor =serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()
    class Meta:
        model = Unit
        fields  = '__all__'
    
    def get_tutor(self, obj):
        if obj.tutor:
            return {
                "first name": obj.tutor.first_name,
                "last name": obj.tutor.last_name
            }
        return None

    def get_course(self, obj):
        if obj.course:
            return {
                "title": obj.course.title,
                "description": obj.course.description
            }
        return None