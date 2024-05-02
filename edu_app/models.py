from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=False)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='taught_courses')
    students = models.ManyToManyField(User, related_name='enrolled_courses')
    course_file = models.FileField(upload_to='course_materials/')
    classes = models.ManyToManyField('Classroom')
    
    def __str__(self):
        return self.name


class Classroom(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classrooms = models.ManyToManyField(Classroom)
    
    def __str__(self):
        return self.user.username


class Notification(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.student.user.username} - {self.message}"

