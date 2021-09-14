from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User



class CustomUser(AbstractUser):
	is_student = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)


	



