
from django.contrib import admin
from .models import *
# Register your models here.


class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch_name','email')
    search_fields=('branch_name',)
admin.site.register(Branch,BranchAdmin)



class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    search_fields=('name',)
admin.site.register(Teacher,TeacherAdmin)