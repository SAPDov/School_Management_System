from django.shortcuts import render
from django.views.generic.list import ListView
from courses.models import Course
from .models import Student




class CourseListView(ListView):
	model = Course
	template_name = 'students/student_course_list.html'
	

	def get_queryset(self):
		return self.request.user.student.student_courses.all()








