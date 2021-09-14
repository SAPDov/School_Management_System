from django.urls import path
from . import views 
from teachers.views import CourseListView

urlpatterns = [
	path('t_course_list', CourseListView.as_view(), name='t_course_list'),
	  
]