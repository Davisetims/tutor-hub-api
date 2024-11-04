from rest_framework import viewsets, permissions
from tutor_availability.models import TutorAvailability
from tutor_availability.serializers import TutorAvailabilitySerializer

class TutorAvailabilityViewSet(viewsets.ModelViewSet):
    serializer_class = TutorAvailabilitySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = TutorAvailability.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_tutor:
            return TutorAvailability.objects.filter(tutor=user)
        else:
            return TutorAvailability.objects.none()  
