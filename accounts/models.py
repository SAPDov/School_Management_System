from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User



class CustomUser(AbstractUser):
	is_student = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)

#create a profile for StudentUser and TeacherUser
	def profile(self):
		if self.is_student:
			return self.student

		elif self.is_teacher:
			return self.teacher





