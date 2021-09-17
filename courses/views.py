from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from .models import Course, Comment
from students.models import Student
from .forms import CommentForm

# Create your views here.


class CourseListView(ListView):
	model = Course

	
class CourseDetailView(DetailView):
	model = Course
	template_name = 'courses/course_detail.html'
	

# class AddCommentView(CreateView):
# 	model = Comment
# 	template_name = 'courses/add_comment.html'
# 	form_class = CommentForm 





# 	def form_valid(self, form):
# 		form.instance.comment = self.request.user.profile()
# 		return super().form_valid(form)


# 	success_url = reverse_lazy('course-detail')


class CourseDetailView(DetailView):
	model = Course
	template_name = 'courses/course_detail.html'

	# form_class = CommentForm 
	# success_url = reverse_lazy('detail')

	def get_context_data(self, **kwargs):
		context = super(CourseDetailView, self).get_context_data(**kwargs)
		context['form'] = CommentForm()
		context['comment'] = Comment.objects.all()
		print(context)
		return context

	
class CommentCreateView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'courses/add_comment.html'


	def get_success_url(self):
		return reverse('detail:comment', kwargs={'pk': self.object.pk})

	
	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)


	def form_valid(self, form):
		self.object = self.get_object()
		print(self.object)
		form.instance.student = self.request.user.profile()
		form.instance.comments = Comment.objects.get(pk=self.object.pk)
		# form.instance.created = timezone.now
		form.save()
		return super(CourseDetailView, self).form_valid(form)


# 	def post(self, request, *args, **kwargs):
# 			self.object = self.get_object()

# 			if 'form' in request.POST:
# 				form_class = self.get_form_class()
# 				form_name = 'form'
# 			form = self.get_form(form_class)


# 			success_url = self.get_success_url()
# 			self.object.deleted = False
# 			self.object.save()
# 			return HttpResponseRedirect(success_url)
# 		except:
# 			pass
# 		return super(CreateView, self).post(request, *args, **kwargs)

# 	def form_valid(self, form):
# 		self.object = self.get_object()
# 		comm = form.save(commit=False)
# 		comm.student = self.request.user
# 		comm.course_name = self.object.comments.name
# 		comm.course_name_id = self.object.id
# 		comm.save()
# 		return HttpResponseRedirect(self.get_success_url())



	# def form_valid(self, form):
	# 	comment = form.save(commit=False)
	# 	comment.created_by = self.request.user.profile()
	# 	comment.save()
	# 	return super().form_valid(form)


	# # def get_form(self, form_class=None):
	# # 	form = super().get_form(form_class)
	# # 	return form
	# 	self.object = form.save(commit=False)
 #        self.object.user = self.request.user
 #        self.object.save()
 #        return HttpResponseRedirect(self.get_success_url())	
	



	

# def post(self, request, *args, **kwargs):
# 	self.object = None
# 	return super().post(request, *args, **kwargs)





		# def post(self, request, *args, **kwargs):
		# form = self.form_class(request.POST)
		# if form.is_valid():
		# 	# <process form cleaned data>
		# 	return HttpResponseRedirect('/success/')

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(CourseDetailView, self).get_context_data(*args, **kwargs)
	# 	context['course_list'] = Course.objects.all()
	# 	return context

