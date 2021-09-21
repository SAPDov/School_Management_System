from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import CreateView
from courses.models import Course, Lesson, Attendance
from .models import Teacher
from students.models import Student
from django.urls import reverse_lazy
from .forms import AttendanceFormset, Attendanceform, Lessonform
from django.forms import modelformset_factory
from bootstrap_datepicker_plus import DateTimePickerInput



class CourseListView(ListView):
	model = Course
	template_name = 'teachers/teacher_course_list.html'
	
	def get_queryset(self):
		return self.request.user.teacher.teacher_courses.all()
		
	def get(self, request, *args, **kwargs):
		if self.request.user.is_student:
			return redirect('s_course_list')
		return super().get(request, *args, **kwargs)


class LessonCreateView(CreateView):
	model = Lesson
	form_class = Lessonform
	template_name = 'teachers/add_lesson.html'
	success_url = reverse_lazy('lesson_list')

	def get_course(self):
		course_id = self.kwargs['pk']
		return get_object_or_404(Course, id=course_id)

	def get_context(self, **kwargs):
		context = super().get_context_data(**kwargs)		
		context['course'] = self.get_course()
		print(context)
		return context

	def get_form(self):
		form = super().get_form()
		form.fields['start_time'].widget = DateTimePickerInput()
		return form


	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.teacher = self.request.user.profile()
		self.object.course = self.get_course()
		self.object.save()
		return super().form_valid(form)



class AttendanceCreateView(CreateView):
	model = Attendance
	form_class = Attendanceform
	template_name = 'teachers/add_attendance.html'
	# success_url = reverse_lazy('lesson_list')


	def get_context_data(self, **kwargs):
		context = super(AttendanceCreateView, self).get_context_data(**kwargs)		
		context['lesson'] = self.lesson = Lesson.objects.get(id=self.kwargs['id'])
		AttendanceFormset = modelformset_factory(Attendance, fields=['student','status'], extra=self.lesson.course.student.count())
		context['formset'] = AttendanceFormset(
		queryset=Attendance.objects.none(), 
		initial=[{'student':student.id} for student in self.lesson.course.student.all()])
		return context

	def get_lesson(self):
		lesson_id = self.kwargs['id']
		return get_object_or_404(Lesson, id=lesson_id)


	def post(self, request, *args, **kwargs):
		formset = AttendanceFormset(request.POST, request.FILES)
		# lesson = Lesson.objects.get(id=self.kwargs['id'])

		if formset.is_valid():
			return self.form_valid(formset)


	def form_valid(self, formset):
		instances = formset.save(commit=False)
		for instance in instances:
			instance.teacher = self.request.user.profile()
			instance.lesson = self.get_lesson()
			# print(instance.object)
			instance.save()
		return redirect('lesson_list')




	# def add_attendance(request):
	
	# 	formset = AttendanceFormset(queryset=Attendance.objects.none())
	# 	# request.user.profile.animal_set.all()
	# 	# Animal.objects.filter(created_by = request.user.profile)
	# 	if request.method == 'POST':
	# 		formset = AttendanceFormset(request.POST, queryset=request.user.profile.attendance_set.all())
	# 		if formset.is_valid():
	# 			for form in formset:
				
	# 				if form.cleaned_data:
	# 					status = form.save(commit=False)
	# 					status.teacher = request.user.profile
	# 					status.save()
	# 			return redirect('lesson_detail', attendance.lesson.id)
	# 	return render(request, 'add_attendance.html', {'formset':formset}) 




	# def get(self, request, *args, **kwargs):
	# 	if self.request.user.is_student:
	# 		return redirect('s_course_list')
	# 	return super().get(request, *args, **kwargs)








	
# 	# def get_lesson(self):
# 	# 	lesson_id = self.kwargs['pk']
# 	# 	return get_object_or_404(Lesson, id=lesson_id)

# 	# def get_course(self):
# 	# 	course_id = self.kwargs['pk']
# 	# 	return get_object_or_404(Course, id=course_id)


# 	def get_context_data(self, **kwargs):
# 		context = super(AttendanceCreateView, self).get_context_data(**kwargs)
# 		context['formset'] = AttendanceFormset(queryset=Attendance.objects.none(), instance=Teacher.objects.get(id=self.request.user.id), initial=[{'student': student} for student in self.get_initial()['students']])

# 		return context

# 	def get_initial(self):
# 		teacher_id = self.request.user.id
# 		teacher = Teacher.objects.get(id=teacher_id)
# 		initial = super(AttendanceCreateView, self).get_initial()
# 		initial['students'] = Student.objects.all()
# 		return initial


# 	def form_valid(self, formset):
# 		attendance = formset.save(commit=False)
# 		# attendance.lesson = self.get_lesson()
# 		# attendance.course = self.get_course()
# 		attendance.save()
# 		return redirect('lesson_detail', attendance.lesson.id)


# 	# def form_valid(self, formset):
# 	# 	comment = form.save(commit=False)
# 	# 	# print(comment)
# 	# 	comment.student = self.request.user.profile()
# 	# 	# print(self.get_course())
# 	# 	comment.course_name = self.get_course()
# 	# 	# print(comment.comments_id)
# 	# 	comment.save()
# 	# 	return redirect('course_detail', comment.course_name.id)
# # success_url = reverse_lazy('lesson_detail')

