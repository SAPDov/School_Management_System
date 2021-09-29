from django.urls import path, include
from . import views 
from students.views import CourseListView, StudentListView

urlpatterns = [
	path('all_students', StudentListView.as_view(), name='all_students'),
    path('s_course_list', CourseListView.as_view(), name='s_course_list'),
      
]


