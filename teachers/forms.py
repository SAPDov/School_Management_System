from django import forms
from django.forms import ModelForm
from .models import Teacher
from courses.models import Attendance, Lesson                      
from django.forms import modelformset_factory, inlineformset_factory, widgets



class TeacherProfileForm(ModelForm):
	class Meta:
		model = Teacher
		fields = ['phone', 'image', 'address']


class Lessonform(ModelForm):
	class Meta:
		model = Lesson
		exclude = ['course']



class Attendanceform(ModelForm):
	class Meta:
		model = Attendance
		fields = ['lesson', 'student','status']


AttendanceFormset = modelformset_factory(Attendance, fields=['student','status'])

