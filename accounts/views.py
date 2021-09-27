from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from students.forms import StudentProfileForm
from teachers.forms import TeacherProfileForm
from students.models import Student
from .forms import RegisterForm, UserUpdateForm

# Create your views here.

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)   
		if form.is_valid():
			if User.objects.filter(username=form.cleaned_data['username']).exists():
				messages.errors(request, f'Username already exists')
			elif User.objects.filter(email=form.cleaned_data['email']).exists():
				messages.errors(request, f'Email already exists')
	
			elif form.cleaned_data['password1'] != form.cleaned_data['password2']:
				messages.errors(request, f'Passwords do not match')
		
			form.save()
# send a sucessfull email after registration
			form.send()         
			username = form.cleaned_data['username']
			password1 = form.cleaned_data['password1']

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
		u_form = UserUpdateForm(request.POST,instance=request.user)
		if request.user.is_student:
			p_form = StudentProfileForm(request.POST, request.FILES, instance=request.user.profile())
		elif request.user.is_teacher:
			p_form = TeacherProfileForm(request.POST, request.FILES, instance=request.user.profile())

		if p_form.is_valid() and u_form.is_valid():
			u_form.save()
			p_form.save()
		
			messages.success(request, 'Your Profile has been updated!')
			return redirect('profile')
		else:
			print(u_form.errors, p_form.errors)
	else:
		u_form = UserUpdateForm(instance=request.user)

		if request.user.is_student:
			p_form = StudentProfileForm(instance=request.user.profile())
		
		elif request.user.is_teacher:
			p_form = TeacherProfileForm(instance=request.user.profile())
			
		
	context = {
	'u_form': u_form, 
	'p_form': p_form,
	}

	return render(request, 'accounts/edit_profile.html', context)

	# context = {'u_form': u_form, 'p_form': p_form}



#move to the pages app
class ClickView(TemplateView):
	template_name = 'accounts/click_view.html'


class Dashboard(ListView):
	template_name = 'accounts/dashboard.html'
	model = Student
	paginate_by = 2
	
# Query a list of students for a specific teacher via course

	def get_queryset(self):
		if self.request.user.is_teacher:
			courses = self.request.user.teacher.teacher_courses.all()
			q = Student.objects.filter(id__in=courses)
		return q


	def get_context_data(self, **kwargs):
		context = super(Dashboard, self).get_context_data(**kwargs)
		context['courses'] = self.request.user.teacher.teacher_courses.all()
		return context




			

	




