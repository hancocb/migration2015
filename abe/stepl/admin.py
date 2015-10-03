from django.contrib import admin

from .models import IndexInput
from .models import CountyData


class MemberAdmin(admin.ModelAdmin):
    list_display = ("state_name","name","station_name")
    search_fields = ['state_name']

admin.site.register(CountyData, MemberAdmin)
admin.site.register(IndexInput)
