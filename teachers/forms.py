from django import forms
from django.forms import ModelForm
from .models import Teacher
from courses.models import Attendance, Lesson                      
from django.forms import modelformset_factory, inlineformset_factory, widgets
from bootstrap_datepicker_plus import DateTimePickerInput, TimePickerInput



class TeacherProfileForm(ModelForm):
	class Meta:
		model = Teacher
		fields = ['phone', 'image', 'address']


class LessonForm(ModelForm):
	class Meta:
		model = Lesson
		exclude = ['course']
		start_time = forms.DateTimeField(
			widget = DateTimePickerInput(format='%m/%d/%Y %H:%M'))
			


			  # default date-format %m/%d/%Y will be used
			# 'end_date': TimePickerInput(format='%m/%d/%Y') # specify date-frmat
		
	

class Attendanceform(ModelForm):
	class Meta:
		model = Attendance
		fields = ['lesson', 'student','status']


AttendanceFormset = modelformset_factory(Attendance, fields=['student','status'])

