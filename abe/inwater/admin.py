from django.contrib import admin

# Register your models here.
from .models import *

class MonitoringAdmin(admin.ModelAdmin):
    list_display = ("gid", "name", "agency_type")
    ordering = ["name", "gid"]
    search_fields = ['agency_type','agency_organization','name','description','user_email']

admin.site.register(Monitoring, MonitoringAdmin)