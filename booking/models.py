from django.db import models
from django.core.exceptions import ValidationError
from tutor_availability.models import TutorAvailability
from users.models import User
from courses.models import Unit



class Booking(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'pending', 'Pending'
        ACCEPTED = 'accepted', 'Accepted'
        DECLINED = 'declined', 'Declined'

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    tutor_availability = models.ForeignKey(TutorAvailability, on_delete=models.CASCADE, related_name="bookings")
    unit = models.ManyToManyField(Unit, related_name="bookings")
    requested_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    
    def save(self, *args, **kwargs):
    
        if  self.student.is_tutor==True:
            raise ValidationError("The selected user is not a student.")
        super().save(*args, **kwargs) 

    def __str__(self):
        return f"Booking for {self.student.username} with {self.tutor_availability.tutor.username}"
