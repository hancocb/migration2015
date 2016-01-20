from django.contrib import admin

# Register your models here.
from .models import *

class MonitoringAdmin(admin.ModelAdmin):
    list_display = ("gid", "name", "agency_type")
    ordering = ["name", "gid"]

admin.site.register(Monitoring, MonitoringAdmin)