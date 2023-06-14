from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Subject(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True, unique=False, default="")

class StudentProfile(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    student_class = models.CharField(max_length=50, blank=True, null=True, unique=False, default="")
    gender = models.CharField(max_length=50, blank=True, null=True, unique=False, default="")
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True, unique=False, default="")
    date_created = models.DateTimeField(auto_now_add=True)

class ParentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='parent_profile')
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='parent_profile')
    date_created = models.DateTimeField(auto_now_add=True)

class TeacherProfile(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='teacher_profile')
    teacher_class = models.CharField(max_length=50, blank=True, null=True, unique=False, default="")
    gender = models.CharField(max_length=50, blank=True, null=True, unique=False, default="")
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True, unique=False, default="")
    date_created = models.DateTimeField(auto_now_add=True)

class PrincipalProfile(models.Model):
    principal = models.OneToOneField(User, on_delete=models.CASCADE, related_name='principal_profile')
    principal_class = models.CharField(max_length=50, blank=True, null=True, unique=False, default="")
    gender = models.CharField(max_length=50, blank=True, null=True, unique=False, default="")
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True, unique=False, default="")
    date_created = models.DateTimeField(auto_now_add=True)

class Note(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='student_note')
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, related_name='teahcer_note')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='note')
    note = models.CharField(max_length=50, blank=True, null=True, unique=False, default="")
    date_created = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message')
    broadcast = models.BooleanField(default=False)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver_message')
    message_title = models.CharField(max_length=50, blank=True, null=True, unique=False, default="")
    message = models.TextField(blank=True, null=True, unique=False, default="")
    date_created = models.DateTimeField(auto_now_add=True)

class Payment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='payment', null=True, blank=True)
    amount = models.CharField(max_length=50, blank=True, null=True, unique=False, default="")
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

class TeacherSalary(models.Model):
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, related_name='teacher_salary')
    amount = models.CharField(max_length=50, blank=True, null=True, unique=False, default="")
    reason = models.CharField(max_length=50, blank=True, null=True, unique=False, default="")
    month = models.CharField(max_length=50, blank=True, null=True, unique=False, default="")
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)