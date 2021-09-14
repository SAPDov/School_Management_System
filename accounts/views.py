from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.contrib import messages
# from django.contrib.messages import constants as messages
from students.forms import StudentProfileForm
from teachers.forms import TeacherProfileForm
from .forms import RegisterForm

# Create your views here.


def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password1 = form.cleaned_data.get('password1')
			user = authenticate(username=username, password1=password1)
			if user:
				login(request, user)
				messages.success(request, f'Your account has been created! You are now able to log in')
			return redirect('login')
	else:
		form = RegisterForm()
	return render(request, 'accounts/register.html', {'form': form})



@login_required
def profile(request):
	return render(request, 'accounts/profile.html')


def edit_profile(request):
	if request.method == 'POST':
		u_form = RegisterForm(request.POST,instance=request.user)
		if request.GET['is_student']:
			p_form = StudentProfileForm(request.POST,request.FILES,instance=request.user.profile)
		elif request.GET['is_teacher']:
			p_form = TeacherProfileForm(request.POST,request.FILES,instance=request.user.profile)

		if p_form.is_valid() and u_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,'Your Profile has been updated!')
			return redirect('accounts/profile')
	else:
		p_form = ProfileUpdateForm(instance=request.user)
		u_form = UserUpdateForm(instance=request.user.profile)

	context={'p_form': p_form, 'u_form': u_form}
	return render(request, 'edit_profile.html', context)


#move to the pages app
class ClickView(TemplateView):
	template_name = 'accounts/click_view.html'


class Dashboard(TemplateView):
	template_name = 'accounts/dashboard.html'


	

# def login_redirect(request):
# 	if request.user.is_student:
# 		# change unique
# 		return redirect('students/s_dashboard')
# 	else:
# 		return redirect('teachers/t_dashboard')





# class UpdateProfile(UpdateView):

# 	model = Student



