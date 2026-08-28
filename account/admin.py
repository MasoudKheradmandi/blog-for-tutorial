from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class MyUserAdmin(UserAdmin):
    model = User
    list_display = ('phone_number', 'is_staff', 'is_active','is_superuser')
    list_filter = ('is_staff', 'is_active')
    
    fieldsets = (
        ('PersonalInfo', {'fields': ('phone_number', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    

    add_fieldsets = (
        (None, {
            'classes': ('User',),
            'fields': ('phone_number',),
        }),
    )
    search_fields = ('phone_number',)
    ordering = ('id',)

admin.site.register(User, MyUserAdmin)
