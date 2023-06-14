from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import date
from django.utils.translation import gettext as _

class User(AbstractUser):
	username = models.CharField(
        max_length=50, blank=True, null=True, unique=False, default="")
	email = models.EmailField(_('email address'), unique = True)
	phone_number = models.CharField(max_length=15, null=True, blank=True)
	first_name = models.CharField(max_length=50, blank=True, null=True, unique=False, default="")
	last_name = models.CharField(max_length=50, blank=True, null=True, unique=False, default="")
	admin = models.BooleanField(default=False)
	student = models.BooleanField(default=False)
	principal = models.BooleanField(default=False)
	parent = models.BooleanField(default=False)
	teacher = models.BooleanField(default=False)
	profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
	def __str__(self):
		return str(self.email)
	