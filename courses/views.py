from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Course

# Create your views here.
def info(request):
	return render(request, 'courses/info.html')


class CourseListView(ListView):
	model = Course
	

class CourseDetailView(DetailView):
	model = Course

	def get_context_data(self, *args, **kwargs):
		context = super(CourseDetailView, self).get_context_data(*args, **kwargs)
		context['course_list'] = Course.objects.all()
		return context

