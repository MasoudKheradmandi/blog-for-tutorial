from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Profile

class MyUserAdmin(UserAdmin):
    model = User
    list_display = ('phone_number', 'is_staff', 'is_active','is_superuser','password')
    list_filter = ('is_staff', 'is_active')
    
    fieldsets = (
        ('PersonalInfo', {'fields': ('phone_number', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2'),
        }),
    )
    search_fields = ('phone_number',)
    ordering = ('id',)

admin.site.register(User, MyUserAdmin)


class AdminProfile(admin.ModelAdmin):
    list_display = ['user','email',]
    search_fields = ['email',]
admin.site.register(Profile,AdminProfile)