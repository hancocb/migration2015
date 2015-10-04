from django.contrib import admin

from .models import IndexInput,CountyData,CountyDataInput,SoilData,SoilDataInput


class CountyDataAdmin(admin.ModelAdmin):
    list_display = ("state_name","name")
    search_fields = ['state_name']

class IndexInputAdmin(admin.ModelAdmin):
    list_display = ("id","num_watershd","num_gully","num_steambank")

admin.site.register(CountyData, CountyDataAdmin)
admin.site.register(CountyDataInput, CountyDataAdmin)
admin.site.register(IndexInput, IndexInputAdmin)

admin.site.register(SoilData)
admin.site.register(SoilDataInput)
