from django.db import models
from django.core.exceptions import ValidationError
from users.models import User

class TutorAvailability(models.Model):
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="availabilities")
    day_of_week = models.CharField(
        max_length=9,
        choices=[
            ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
            ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'),
            ('Sunday', 'Sunday')
        ]
    )
    hourly_rate = models.FloatField()
    
    def save(self, *args, **kwargs):
        
        if not self.tutor.is_tutor:
            raise ValidationError("The selected user is not a tutor.")
        super().save(*args, **kwargs) 


    def __str__(self):
        return f"{self.tutor.username} - {self.day_of_week} (${self.hourly_rate}/hr)"