from rest_framework.routers import DefaultRouter
from tutor_availability.views import TutorAvailabilityViewSet

tutor_router = DefaultRouter()
tutor_router.register(r'tutor/availability', TutorAvailabilityViewSet)

urlpatterns = [
    
]
urlpatterns += tutor_router.urls
