from django.contrib import admin

# Register your models here.
from myform.models import student

class studentadmin(admin.ModelAdmin):
    list_display=['empid','empname','empage','empsalary']
admin.site.register(student,studentadmin)
