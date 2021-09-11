from django.shortcuts import render
from django.views.generic.base import TemplateView
from courses.models import Course

# Create your views here.



class Dashboard(TemplateView):
	template_name = 'students/dashboard.html'










