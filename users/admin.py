from django.contrib import admin
from .models import User
# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display = ('acount_name', 'registered_date')

admin.site.register(User)