from django.contrib import admin

from .models import CustomUser


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['id', 'username', 'email']


admin.site.register(CustomUser, UserAdmin)
