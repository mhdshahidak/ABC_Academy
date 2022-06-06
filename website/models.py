from django.db import models
from adminapp.models import Branch
from phone_field import PhoneField

# Create your models here.

class OnlineApplying(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = PhoneField()
    gender = models.CharField(max_length=20)
    dob = models.DateField()
    course = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True)
    address = models.TextField()
    city = models.CharField(max_length=50,default="")
    country = models.CharField(max_length=60,default="")
    pin = models.BigIntegerField()
