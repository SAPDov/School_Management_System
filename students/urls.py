from django.urls import path, include
from . import views 
from students.views import Dashboard

urlpatterns = [
    path('dashboard', Dashboard.as_view(), name='s_dashboard'),
      
]