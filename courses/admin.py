from django.contrib import admin
from courses.models import Course, Unit

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description', 'created_at')
    
class UnitAdmin(admin.ModelAdmin):
    list_display = ('id','course','unit_name', 'description', 'tutor',  'created_at')
    
admin.site.register(Course,CourseAdmin)
admin.site.register(Unit, UnitAdmin)
