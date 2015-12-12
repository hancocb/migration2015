from django.contrib import admin

# Register your models here.


from .models import *



def changeIsShown(modeladmin, request, queryset):
    for showItem in queryset:
        showOrNot = not showItem.isShown
        showItem.isShown = showOrNot
        showItem.save()

changeIsShown.short_description = "Show / Unshow"

class AdminListDisplayAdmin(admin.ModelAdmin):
    list_display = ("ClassName", "FieldName", "isShown")
    ordering = ["ClassName", "FieldName"]
    actions = [changeIsShown]

admin.site.register(AdminListDisplay, AdminListDisplayAdmin)
