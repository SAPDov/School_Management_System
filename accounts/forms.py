from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser
from django.core.mail import send_mail
from django.conf import settings


class RegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)
	is_student = forms.BooleanField(label='Student',required=False)
	is_teacher = forms.BooleanField(label='Teacher', required=False)
					
	class Meta:
		model = CustomUser
		fields = ['username', 'first_name','last_name', 'email', 'password1', 'password2', 'is_student', 'is_teacher']


	def get_info(self):
		"""
		Method that returns formatted information
		:return: subject, msg
		"""
		# Cleaned data
		cl_data = super().clean()

		name = cl_data.get('username').strip()
		from_email = cl_data.get('email')

		msg = f'{name} with email {from_email}'


		return msg

	def send(self):

		msg = self.get_info()

		send_mail(
			subject='Hello',
			message=msg,
			from_email=settings.EMAIL_HOST_USER,
			recipient_list=[settings.RECIPIENT_ADDRESS])

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ['first_name','last_name', 'email']

