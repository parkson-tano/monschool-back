from .serializers import *
from .models import *
from rest_framework import viewsets

class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

class StudentProfileViewSet(viewsets.ModelViewSet):
    serializer_class = StudentProfileSerializer
    queryset = StudentProfile.objects.all()

class ParentProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ParentProfileSerializer
    queryset = ParentProfile.objects.all()

class TeacherProfileViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherProfileSerializer
    queryset = TeacherProfile.objects.all()

class PrincipalProfileViewSet(viewsets.ModelViewSet):
    serializer_class = PrincipalProfileSerializer
    queryset = PrincipalProfile.objects.all()

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


# Compare this snippet from main\views.py:

    
class SubjectFetchViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    def get_queryset(self):
        title_name = self.request.query_params.get('title_name')
        return Subject.objects.filter(title=title_name)
    
class StudentProfileFetchViewSet(viewsets.ModelViewSet):
    serializer_class = StudentProfileSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        return StudentProfile.objects.filter(user=user_id)

class StudentProfileFetchByClassViewSet(viewsets.ModelViewSet):
    serializer_class = StudentProfileSerializer
    def get_queryset(self):
        student_class = self.request.query_params.get('student_class')
        return StudentProfile.objects.filter(student_class=student_class)

class ParentProfileFetchViewSet(viewsets.ModelViewSet):
    serializer_class = ParentProfileSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        return ParentProfile.objects.filter(user=user_id)
    
class TeacherProfileFetchViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherProfileSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        return TeacherProfile.objects.filter(user=user_id)
    
class PrincipalProfileFetchViewSet(viewsets.ModelViewSet):
    serializer_class = PrincipalProfileSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        return PrincipalProfile.objects.filter(user=user_id)
    
class NoteFetchViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    def get_queryset(self):
        student_id = self.request.query_params.get('student_id')
        return Note.objects.filter(student=student_id)

class MessageFetchViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    def get_queryset(self):
        sender_id = self.request.query_params.get('sender_id')
        receiver_id = self.request.query_params.get('receiver_id')
        return Message.objects.filter(sender=sender_id, receiver=receiver_id)
    
class PaymentFetchViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    def get_queryset(self):
        student_id = self.request.query_params.get('student_id')
        return Payment.objects.filter(student=student_id)

class TeacherSalaryFetchViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSalarySerializer
    def get_queryset(self):
        teacher_id = self.request.query_params.get('teacher_id')
        return TeacherSalary.objects.filter(teacher=teacher_id)
    
# Compare this snippet from main\views.py: