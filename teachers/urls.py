from . import views 
from teachers.views import Dashboard

urlpatterns = [
    path('dashboard', Dashboard.as_view(), name='dashboard'),
      
]