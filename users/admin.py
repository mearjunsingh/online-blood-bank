from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomUserAdmin(UserAdmin):
    ordering = ['-date_joined']
    list_display = ['email', 'blood_group', 'phone_number', 'district', 'is_donor']
    search_fields = ['email', 'phone_number', 'district', 'local_level']
    list_filter = ['blood_group', 'gender', 'is_donor']
    add_fieldsets = (
        (None, {
            'fields' : (
                'email',
                'password1', 'password2',
            )
        }),
        ('Personal', {
            'fields' : (
                ('first_name', 'last_name'),
                'phone_number',
                'date_of_birth',
                ('blood_group', 'gender'),
                ('district', 'local_level')
            )
        })
    )
    fieldsets = (
        ('Meta', {
            'fields' : (
                'is_donor',
                'email', 
                ('first_name', 'last_name')
            )
        }),
        ('Personal', {
            'fields': (
                'display_photo',
                'phone_number',
                'date_of_birth',
                ('blood_group', 'gender'),
                ('district', 'local_level')
                )
        }),
        ('Details', {
            'fields': (
                'is_staff',
                'is_active',
                'date_joined',
                'last_login'
                )
        }),
        ('Permissions', {
            'classes' : ('collapse',),
            'fields' : (
                ('groups'),
                ('user_permissions')
            )
        })
    )
    list_per_page = 100


admin.site.register(CustomUser, CustomUserAdmin)