from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Users,Hood

admin.site.register(Users)
admin.site.register(Hood)