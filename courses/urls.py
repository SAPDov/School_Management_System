from django.urls import path, include
from . import views 
from courses.views import CourseListView,  CourseDetailView, CommentCreateView


urlpatterns = [	
   path('course-list', CourseListView.as_view(), name='course-list'),
   path('courses/<int:pk>/', CourseDetailView.as_view(), name='detail'),
   path('courses/<int:pk>/comment', CommentCreateView.as_view(), name='comment'),
       
]