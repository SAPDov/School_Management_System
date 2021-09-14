from django.contrib import admin
from courses.models import Course, Lesson, Days
# Register your models here.
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Days)