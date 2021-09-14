from django.urls import path, include
from . import views 
from students.views import CourseListView

urlpatterns = [
    path('s_course_list', CourseListView.as_view(), name='s_course_list'),
      
]


