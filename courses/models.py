from django.db import models
from students.models import Student
from teachers.models import Teacher

# Create your models here.

class Course(models.Model):
	name = models.CharField(max_length=70)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	student = models.ManyToManyField(Student, related_name='student_courses')
	teacher = models.ManyToManyField(Teacher, related_name='teacher_courses')

	def __str__(self):
		return self.name


	# teacher = models.ForeignKey(Teacher, related_name="classes")
 #    course = models.ForeignKey(Course, related_name="classes")

	# 