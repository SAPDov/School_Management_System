from django import forms
from django.forms import ModelForm
from .models import Student



class StudentProfileForm(ModelForm):
	class Meta:
		model = Student
		fields = ['phone', 'image', 'address', 'about', 'fb_url', 'twitter_url', 'instagram_url']


