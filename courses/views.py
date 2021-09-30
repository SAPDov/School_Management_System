from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from .models import Course, Comment, Lesson, Attendance
from students.models import Student
from .forms import CommentForm


# All courses
class CourseListView(ListView):
	model = Course
	paginate_by = 3


class CourseDetailView(DetailView):
	model = Course
	template_name = 'courses/course_detail.html'


class CommentCreateView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'courses/add_comment.html'

#Only students can add comments
	def get(self, request, *args, **kwargs):
		if request.user.is_teacher:
			return redirect('course_detail', kwargs['pk'])
		return super().get(request, *args, **kwargs)


	def get_course(self):
		course_id= self.kwargs['pk']
		return get_object_or_404(Course, id=course_id)


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['comment'] = self.get_course()
		return context

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		return form

	def form_valid(self, form):
		comment = form.save(commit=False)
		# print(comment)
		comment.student = self.request.user.profile()
		comment.course = self.get_course()
		# print(comment.comments_id)
		comment.save()
		return redirect('course_detail', comment.course.id)



class LessonListView(ListView):
	model = Lesson
	


	def get_queryset(self):
		if self.request.user.is_teacher:
			courses = self.request.user.teacher.teacher_courses.all()
			q = Lesson.objects.filter(course__in=courses)
			print(q)
		else:
			courses = self.request.user.student.student_courses.all()
			q = Lesson.objects.filter(course__in=courses)
			print(q)
		return q


class LessonDetailView(DetailView):
	model = Lesson
	template_name = 'courses/lesson_detail.html'


	






	# def get_course_name(self):
	# 	course_id = self.kwargs['pk']
	# 	return get_object_or_404(Course, id=course_id)

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['course'] = self.get_course_name()
	# 	# Course.objects.filter(name=self.get_course_name())
	# 	print(context)
	# 	return context


# return self.request.user.teacher.lesson.student_courses.all()