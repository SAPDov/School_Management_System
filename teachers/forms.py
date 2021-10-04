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
		fields = ['course', 'start_time', 'end_time']
		start_time = forms.DateTimeField(
					widget = DateTimePickerInput(format='%m/%d/%Y %H:%M'))
		widgets = {
			'course': forms.HiddenInput,
		}


# overide the form - exculde the course field 
		def __init__(self, *args, **kwargs):
			super(LessonForm, self).__init__(*args, **kwargs)
			inital = kwargs.get('initial')
			course = inital.get('course')
			

			


class Attendanceform(ModelForm):

	class Meta:
		model = Attendance
		fields = ['lesson', 'student', 'status']

AttendanceFormset = modelformset_factory(Attendance, fields=['student','status'])

	