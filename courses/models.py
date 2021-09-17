from django.db import models
from students.models import Student
from teachers.models import Teacher
# from django.urls import reverse


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


	# def get_absolute_url(self):
	# 	return reverse('course-detail', kwargs={'pk': self.pk})


	def __str__(self):
		return self.name

class Lesson(models.Model):
	lessons = models.ForeignKey(Course, null=True, blank=True, on_delete=models.SET_NULL)
	start_time = models.DateTimeField()
	end_time = models.DurationField()

	def __str__(self):
		return self.lessons.name 


class Comment(models.Model):
	course_name = models.ForeignKey(Course, null=True, on_delete=models.CASCADE, related_name='comments')
	comment_name = models.CharField(max_length=100, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
	body = models.TextField(max_length=500)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)

	def __str__(self):
		return self.comment_name

	class Meta:
		ordering = ['-date_added']


