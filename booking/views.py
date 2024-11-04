from rest_framework import viewsets, permissions
from booking.models import Booking
from booking.serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Booking.objects.all()

        if user.is_authenticated:
            if user.is_tutor:
                return queryset.filter(tutor_availability__tutor=user)
            else:
                return queryset.filter(student=user)
        
        return queryset.none()
