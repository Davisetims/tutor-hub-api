from django.contrib import admin
from booking.models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','student', 'tutor_availability', 'unit', 'requested_date', 'status')
    list_filter = ('status', 'tutor_availability', 'unit')
    search_fields = ('student__username', 'unit__unit_name')
    ordering = ('requested_date',)

admin.site.register(Booking, BookingAdmin)
