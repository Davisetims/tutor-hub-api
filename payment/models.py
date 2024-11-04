from django.db import models
from booking.models import Booking
from users.models import User

class Payment(models.Model):
    class PaymentMethod(models.TextChoices):
        CREDIT_CARD = 'credit_card', 'Credit Card'
        MPESA = 'mpesa', 'Mpesa'

    class PaymentStatus(models.TextChoices):
        PENDING = 'pending', 'Pending'
        COMPLETED = 'completed', 'Completed'
        FAILED = 'failed', 'Failed'
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="payments")
    amount = models.FloatField()
    payment_status = models.CharField(max_length=10, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=PaymentMethod.choices)

    def __str__(self):
        return f"Payment for {self.booking} - {self.payment_status} - requested by {self.user.username}"