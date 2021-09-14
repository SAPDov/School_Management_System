from django.shortcuts import render
from django.views.generic.list import ListView
from courses.models import Course
from .models import Teacher

class CourseListView(ListView):
	model = Course
	template_name = 'teachers/teacher_course_list.html'
	
	def get_queryset(self):
		qs = super().get_queryset()
		print(qs)
		filtered_qs = qs.filter(teacher=self.request.user.teacher)
		print(filtered_qs)
		return filtered_qs


