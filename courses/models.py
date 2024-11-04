from django.db import models
from users.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Unit(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="units")
    unit_name = models.CharField(max_length=200)
    description = models.TextField()
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tutored_units")
    students = models.ManyToManyField(User, related_name="enrolled_units")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.unit_name} ({self.course.title})"