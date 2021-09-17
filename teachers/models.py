from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Teacher(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	phone = models.CharField(max_length=30)
	address = models.CharField(max_length=200)
	image = models.ImageField(upload_to='media/', null=True)



	def __str__(self):
		return self.user.username



	