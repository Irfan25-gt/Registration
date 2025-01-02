from django.contrib import admin

# Register your models here.
from .models import student

#admin.site.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = ["name", "status"]
admin.site.register(student,studentAdmin)


