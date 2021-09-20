from django.urls import path, include
from . import views 
from courses.views import CourseListView,  CourseDetailView, CommentCreateView, LessonListView, LessonDetailView


urlpatterns = [	
   path('course-list', CourseListView.as_view(), name='course-list'),
   path('courses/<int:pk>/', CommentCreateView.as_view(), name='course_comment'),
   path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
   path('lesson_list', LessonListView.as_view(), name='lesson_list'),
   path('lesson/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
   
       
]