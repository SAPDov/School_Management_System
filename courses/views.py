from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from .models import Course, Comment
from students.models import Student
from .forms import CommentForm
from django.utils import timezone
from django.views import View



# Create your views here.


class CourseListView(ListView):
	model = Course


class CourseDetailView(DetailView):
	model = Course
	template_name = 'courses/course_detail.html'



class CommentCreateView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'courses/add_comment.html'

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
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
		print(self.get_course())
		comment.course_name = self.get_course()
		# print(comment.comments_id)
		comment.save()
		return redirect('course_detail', comment.course_name.id)


# https://codepen.io/danmv/pen/VBVKOV