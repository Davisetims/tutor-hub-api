from django.contrib import admin
from payment.models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'booking', 'amount', 
                    'payment_status', 'payment_date', 
                    'payment_method')
    
admin.site.register(Payment,PaymentAdmin)
