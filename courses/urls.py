from django.urls import path, include
from . import views 
from courses.views import CourseListView, CourseDetailView


urlpatterns = [	
   path('info', views.info, name='info'),
   path('course-list', CourseListView.as_view(), name='course-list'),
   path('/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
       
]