from django.shortcuts import render
from django.views.generic.list import ListView
from courses.models import Course
from .models import Student



# Create your views here.


# class Dashboard(TemplateView):
# 	template_name = 'students/s_dashboard.html'


class CourseListView(ListView):
	model = Course
	template_name = 'students/student_course_list.html'
	
	def get_queryset(self):
		qs = super().get_queryset()
		filtered_qs = qs.filter(student=self.request.user.student)
		return filtered_qs






	# def get_context_data(self, *args, **kwargs):
	# 	context = super(CourseListView, self).get_context_data(*args, **kwargs)
	# 	context['student_courses'] = Course.objects.all()
	# 	print(context)
	# 	return context



	# def get(self, request, *args, **kwargs):
	# 	course = Course.objects.all()
	# 	context = {'course': course}
	# 	return render(request, "book-list.html", context=context)


	# # def get_context_data(self, **kwargs):
	# # 	context = super().get_context_data(**kwargs)
	# # 	context['post'] = self.get_post()
	# # 	return context




