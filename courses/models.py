from django.db import models
from students.models import Student
from teachers.models import Teacher
from .helper import duration
from django.urls import reverse



# Create your models here.

class Days(models.Model):
	name = models.CharField(max_length=10)

	def __str__(self):
		return self.name


class Course(models.Model):
	name = models.CharField(max_length=70)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	student = models.ManyToManyField(Student, related_name='student_courses')
	teacher = models.ManyToManyField(Teacher, related_name='teacher_courses')
	start_date = models.DateField(null=True)
	end_date = models.DateField(null=True)
	days = models.ManyToManyField(Days)


	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name


class Lesson(models.Model):

	course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.SET_NULL, related_name='lessons')
	start_time = models.DateTimeField()
	end_time = models.TimeField(null=True, blank=True)
	# student = models.ManyToManyField(Student, related_name='student_lesson')

	def __str__(self):
		return f'{self.course} {self.start_time}'

	# def get_absolute_url(self):
	# 	return reverse('lesson_detail', kwargs={'pk': self.pk })

class Attendance(models.Model):
	# course = models.ForeignKey(Course, on_delete=models.CASCADE)
	# time_stamp = models.DateTimeField(auto_now_add=True)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	status = models.BooleanField(default='True')

	def __str__(self):
		return f'{self.student} {self.course} {self.status}'

class Comment(models.Model):
	course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE, related_name='comments')
	name = models.CharField(max_length=100, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
	body = models.TextField(max_length=500)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)

	def __str__(self):
		return self.body

	class Meta:
		ordering = ['-date_added']


