from rest_framework.routers import DefaultRouter
from booking.views import BookingViewSet

booking_router = DefaultRouter()
booking_router.register(r'session/booking', BookingViewSet)

urlpatterns = [
    
]
urlpatterns += booking_router.urls
