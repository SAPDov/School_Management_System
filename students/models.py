from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from teachers.models import Teacher


# Create your models here.
class Student(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	phone = models.CharField(max_length=30)
	image = models.ImageField(upload_to='media/', null=True, default='static/img/student_img.png')

	def __str__(self):
		return self.user.username




@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
	if created:
		if instance.is_student:
			Student.objects.create(user=instance)
		else:
			Teacher.objects.create(user=instance)

# if you create a profile without a user the below will cause a problem
# @receiver(post_save, sender=CustomUser)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()











	# address = models.CharField(max_length=200)




# class Course(models.Model):
# 	name = models.CharField(max_length=100)
# 	capacity = models.IntegerField(default=15)
# 	date = models.DateTimeField(null=True)
# 	price = models.IntegerField()


# class Student(models.Model):
# 	first_name = models.CharField(max_length=30)
# 	last_name = models.CharField(max_length=30)
# 	telephone = models.CharField(max_length=30)
# 	email = models.EmailField()
# 	address = models.CharField(max_length=200)
# 	is_staff = models.BooleanField(default=False) 
	
# 	dateOfBirth = models.DateField(null=True) 
# 	# level = models.OneToOneDField(Exam, on_delete=models.CASCADA)
# 	course = models.ForeignKey(Course, on_delete=models.SET_NULL)

# class Teacher(models.Model):
# 	first_name = models.CharField(max_length=30)
# 	last_name = models.CharField(max_length=30)
# 	telephone = models.CharField(max_length=30)
# 	is_staff = models.BooleanField(default=True)
# 	email = models.EmailField()
# 	address = models.CharField(max_length=200)
# 	dateStart = models.DateField(auto_now_add=True) 
# 	salary = models.FloatField()
# 	course = models.ManyToManyField(Course) 





# class Exam(models.Model):
# 	question = 
# 	grade = 
# 	student = 
