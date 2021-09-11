from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser


class RegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)
	is_student = forms.BooleanField(label='Student',required=False)
	is_teacher = forms.BooleanField(label='Teacher', required=False)
	
				
	class Meta:
		model = CustomUser
		fields = ['username', 'first_name','last_name', 'email', 'password1', 'password2', 'is_student', 'is_teacher']

	# is_student, is_teacher = forms.TypedChoiceField(coerce=lambda x: bool(int(x)),
	# 			   choices=((0, 'False'), (1, 'True')),
	# 			   widget=forms.RadioSelect
	# 			)

	# 								 widget=forms.RadioSelect(choices=[(True, 'Student'), (False, 'Student')]))
										
									

	# is_teacher = forms.BooleanField(widget=forms.RadioSelect(choices=[(True, 'Teacher')]))
				