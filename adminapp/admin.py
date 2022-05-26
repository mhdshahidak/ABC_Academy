
from django.contrib import admin
from .models import *
# Register your models here.


class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch_name','email')
    search_fields=('branch_name',)
admin.site.register(Branch,BranchAdmin)