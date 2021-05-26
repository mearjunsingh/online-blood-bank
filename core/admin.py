from django.contrib import admin
from django.contrib.admin import ModelAdmin
from . import models


class BloodAdmin(ModelAdmin):
    list_display = ['group', 'slug']


admin.site.register(models.Request)
admin.site.register(models.Blood, BloodAdmin)
admin.site.register(models.District)
admin.site.register(models.LocalLevel)