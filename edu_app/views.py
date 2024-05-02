from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import *
from .serializers import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .permissions import IsTeacher, IsStudent
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.forms import UserCreationForm





class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].required = False  

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if password1:
            if len(password1) < 8:
                raise forms.ValidationError("Şifre en az 8 karakter olmalıdır.")
            return password1

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"] or '123')  
        if commit:
            user.save()
        return user


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, IsStudent]

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, IsTeacher]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=True, methods=['get'])
    def notifications(self, request, pk=None):
        student = self.get_object()
        notifications = Notification.objects.filter(student=student)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)


