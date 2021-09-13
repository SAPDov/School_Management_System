from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

# class TeacherLoginView(LoginView):
# 	template_name = 'teacher/tlogin.html'

# 	def get_success_url(self):
# 		url = self.get_redirect_url()
# 		return url 



class Dashboard(TemplateView):
	template_name = 'teachers/dashboard.html'


