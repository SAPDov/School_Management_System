from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser
from django.core.mail import send_mail
from django.conf import settings


class RegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)
	is_student = forms.BooleanField(label='I am a Student',required=False)
	is_teacher = forms.BooleanField(label='I am a Teacher', required=False)

					
	class Meta:
		model = CustomUser
		fields = ['username', 'first_name','last_name', 'email', 'password1', 'password2', 'is_student', 'is_teacher']


# Send Email After Successfully registered

	def get_info(self):

		cl_data = super().clean()
	
		fname = cl_data.get('first_name').strip()
		lname = cl_data.get('last_name')
		from_email = cl_data.get('email')
		
		msg = f'{fname} {lname} with email {from_email}'
		return msg

	def send(self):
		msg = self.get_info()

		send_mail(
			subject="SchoolMS Sucessfully Registered",
			message=msg,
			from_email=settings.EMAIL_HOST_USER,
			recipient_list=[settings.RECIPIENT_ADDRESS]
			)

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ['first_name','last_name', 'email']

