from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from courses.models import Course
from .models import Teacher

class CourseListView(ListView):
	model = Course
	template_name = 'teachers/teacher_course_list.html'
	
	def get_queryset(self):
		return self.request.user.teacher.teacher_courses.all()
		
	def get(self, request, *args, **kwargs):
		if self.request.user.is_student:
			return redirect('s_course_list')
		return super().get(request, *args, **kwargs)
