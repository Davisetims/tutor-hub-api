from django.urls import path
from courses.views import UserUnitListViewSet, CourseViewSet
from rest_framework.routers import DefaultRouter

unit_router = DefaultRouter()

unit_router.register(r"units",UserUnitListViewSet )
unit_router.register(r"courses", CourseViewSet)

urlpatterns = [
   
]
urlpatterns += unit_router.urls


