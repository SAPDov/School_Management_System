from django import forms
from django.forms import ModelForm
from .models import Teacher



class TeacherProfileForm(ModelForm):
	class Meta:
		model = Teacher
		fields = ['phone', 'image']

