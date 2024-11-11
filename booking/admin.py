from django.contrib import admin
from booking.models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ['student', 'tutor_availability', 'requested_date', 'status', 'get_units']
    
    def get_units(self, obj):
        return ", ".join([unit.unit_name for unit in obj.unit.all()])
    
    get_units.short_description = 'Units'  # Set column name for this field in admin

admin.site.register(Booking, BookingAdmin)


