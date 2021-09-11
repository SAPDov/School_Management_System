from django.urls import path, include
from . import views 
from accounts.views import ClickView

urlpatterns = [
 	path('', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),
   	path("profile", views.profile, name='profile'),
   	path("click", ClickView.as_view(), name='click'),
   	# path("profile", ProfileView.as_view(), name='profile'),
  
        
]