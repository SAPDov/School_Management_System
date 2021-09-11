from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.models import User


admin.site.register(User)
admin.site.register(CustomUser)