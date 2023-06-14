from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Subject)
admin.site.register(StudentProfile)
admin.site.register(ParentProfile)
admin.site.register(TeacherProfile)
admin.site.register(PrincipalProfile)
admin.site.register(Note)
admin.site.register(Message)
admin.site.register(Payment)
admin.site.register(TeacherSalary)
