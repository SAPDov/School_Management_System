from django.urls import path
from . import views 
from teachers.views import CourseListView, AttendanceCreateView, LessonCreateView

urlpatterns = [
	path('t_course_list', CourseListView.as_view(), name='t_course_list'),
	path('add_attendance/<int:id>', AttendanceCreateView.as_view(), name='add_attendance'),
	path('add_lesson/<int:pk>', LessonCreateView.as_view(), name='add_lesson'),
	  
]