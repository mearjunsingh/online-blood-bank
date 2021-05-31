from django.contrib import admin
from django.contrib.admin import ModelAdmin
from . import models


class BloodAdmin(ModelAdmin):
    list_display = ['group', 'slug']


class RequestAdmin(ModelAdmin):
    list_display = ['requested_by', 'blood_group', 'for_date', 'donated_by', 'status']
    list_filter = ['status', 'blood_group']
    date_hierarchy = 'for_date'
    search_fields = ['requested_by__email', 'donated_by__email','requested_by__phone_number', 'donated_by__phone_number', 'district', 'local_level']
    list_per_page = 100


admin.site.register(models.Request, RequestAdmin)
admin.site.register(models.Blood, BloodAdmin)