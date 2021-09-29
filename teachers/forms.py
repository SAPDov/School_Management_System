from django import forms
from django.forms import ModelForm
from .models import Teacher
from courses.models import Attendance, Lesson                      
from django.forms import modelformset_factory, inlineformset_factory, widgets
from bootstrap_datepicker_plus import DateTimePickerInput, TimePickerInput



class TeacherProfileForm(ModelForm):
	class Meta:
		model = Teacher
		fields = ['phone', 'image', 'address', 'about', 'fb_url', 'twitter_url', 'instagram_url']


class LessonForm(ModelForm):
	class Meta:
		model = Lesson
		fields = '__all__'
		start_time = forms.DateTimeField(
			widget = DateTimePickerInput(format='%m/%d/%Y %H:%M'))
			


class Attendanceform(ModelForm):

	class Meta:
		model = Attendance
		fields = ['lesson', 'student', 'status']

AttendanceFormset = modelformset_factory(Attendance, fields=['student','status'])

	