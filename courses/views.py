from rest_framework import permissions, generics, viewsets
from django.db import models
from courses.models import Course, Unit
from courses.serializers import CourseSerializer, UnitSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class UserUnitListViewSet(viewsets.ModelViewSet):
    serializer_class = UnitSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Unit.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Unit.objects.filter(models.Q(tutor=user) | models.Q(students=user)).distinct()
