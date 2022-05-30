
from django.contrib import admin
from .models import *
# Register your models here.


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student','paidamount')
admin.site.register(Payment,PaymentAdmin)
