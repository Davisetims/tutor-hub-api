from django.contrib import admin
from tutor_availability.models import TutorAvailability

class TutorAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('id','tutor', 'day_of_week', 'hourly_rate')

admin.site.register(TutorAvailability, TutorAvailabilityAdmin)