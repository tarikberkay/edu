from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView



urlpatterns = [
    path('courses/', CourseViewSet.as_view({'get': 'list', 'post': 'create'}), name='course-list'),
    path('courses/<int:pk>/', CourseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='course-detail'),
    path('classrooms/', ClassroomViewSet.as_view({'get': 'list', 'post': 'create'}), name='classroom-list'),
    path('classrooms/<int:pk>/', ClassroomViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='classroom-detail'),
    path('students/', StudentViewSet.as_view({'get': 'list', 'post': 'create'}), name='student-list'),
    path('teachers/', TeacherViewSet.as_view({'get': 'list', 'post': 'create'}), name='teacher-list'),
    path('students/<int:pk>/', StudentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='student-detail'),
    path('students/<int:pk>/notifications/', StudentViewSet.as_view({'get': 'notifications'}), name='student-notifications'),

]