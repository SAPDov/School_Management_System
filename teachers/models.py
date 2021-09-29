from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Teacher(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	about = models.TextField(max_length=500, null=True, blank=True)
	phone = models.CharField(max_length=30)
	address = models.CharField(max_length=200)
	image = models.ImageField(upload_to='media/', null=True)
	fb_url = models.CharField(max_length=250, null=True, blank=True)
	twitter_url = models.CharField(max_length=250, null=True, blank=True)
	instagram_url = models.CharField(max_length=250, null=True, blank=True)



	def __str__(self):
		return self.user.username



	