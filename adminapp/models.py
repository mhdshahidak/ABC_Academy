import email
from enum import unique
from django.db import models
from phone_field import PhoneField

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):

        if not email:
            raise ValueError('User must have a email')
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        if user:
            return user
    def create_superuser(self,email,password=None,**extra_fields):

        if not email:
            raise ValueError('User must have a email')
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.is_superuser = True
        user.save(using=self._db)
        return user
class Branch(models.Model):
    branch_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = PhoneField(unique=True)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.BigIntegerField()
    address =  models.TextField()



class Teacher(models.Model):
    gender_choices = (('male','male'),('female','female'),('other','other'))
    teacher_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10,choices=gender_choices)
    dob = models.DateField()
    phone = PhoneField(unique=True)
    email = models.EmailField()
    joining_date = models.DateField()
    qualification = models.CharField(max_length=100)
    experience = models.FloatField()
    address = models.TextField()
    pin = models.BigIntegerField()
    branch = models.ForeignKey(Branch,on_delete=models.PROTECT)


class Student(models.Model):
    gender_choices = (('male','male'),('female','female'),('other','other'))
    student_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10,choices=gender_choices)
    dob = models.DateField()
    phone = PhoneField(unique=True)
    email = models.EmailField()
    address = models.TextField()
    pin = models.BigIntegerField()
    branch = models.OneToOneField(Branch,on_delete=models.PROTECT)

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20,null=True)
    email=models.EmailField(unique=True)
    phone_number=PhoneField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,null=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True)
    Student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    objects = UserManager()
    USERNAME_FIELD='email'




    