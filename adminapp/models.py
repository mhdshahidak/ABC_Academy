import email
from enum import unique
from django.db import models
# from adminapp.views import courses
from phone_field import PhoneField
from tinymce.models import HTMLField

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.template.defaultfilters import date

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
        user.is_staff   = True
        user.save(using=self._db)
        return user


class Courses(models.Model):
    course_id = models.CharField(max_length=50)
    couse_name = models.CharField(max_length=100)
    Duration = models.CharField(max_length=20)
    total_fees = models.FloatField()
    max_students = models.IntegerField(default=0)

    class Meta:
        db_table='courses'


class Batch(models.Model):
    course = models.ForeignKey(Courses,on_delete=models.PROTECT)
    starting_date = models.DateField()
    ending_date = models.DateField()

    class Meta:
        db_table='batch'

class Branch(models.Model):
    branch_id = models.CharField(max_length=20,default="")
    branch_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = PhoneField(unique=True)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.BigIntegerField()
    address =  models.TextField()
    password = models.CharField(max_length=50,default="0")



class Teacher(models.Model):
    gender_choices = (('male','male'),('female','female'),('other','other'))
    teacher_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10,choices=gender_choices)
    dob = models.DateField()
    phone = PhoneField(unique=True)
    email = models.EmailField()
    course = models.ForeignKey(Batch,on_delete=models.PROTECT)
    joining_date = models.DateField()
    qualification = models.CharField(max_length=100)
    city = models.CharField(max_length=100 ,default="")
    state = models.CharField(max_length=100,default="")
    country = models.CharField(max_length=100,default="")
    Password = models.CharField(max_length=100,default="")
    experience = models.FloatField()
    address = models.TextField()
    pin = models.BigIntegerField()
    branch = models.ForeignKey(Branch,on_delete=models.PROTECT)
   
    class Meta:
        db_table = 'name'


class Student(models.Model):
    gender_choices = (('male','male'),('female','female'),('other','other'))
    student_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10,choices=gender_choices)
    dob = models.DateField()
    course = models.ForeignKey(Batch,on_delete=models.PROTECT)
    password = models.CharField(max_length=100,default="")
    fathername = models.CharField(max_length=100,default="")
    fatherphone = models.CharField(max_length=100,default="")
    phone = PhoneField(unique=True)
    email = models.EmailField()
    address = models.TextField()
    branch = models.ForeignKey(Branch,on_delete=models.PROTECT)

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20,null=True)
    email=models.EmailField(unique=True)
    phone_number=PhoneField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,null=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True)
    Student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD='email'



class Exam(models.Model):
    batch = models.ForeignKey(Batch,on_delete=models.PROTECT)
    exam_name = models.CharField(max_length=150)
    exam_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.IntegerField()
    total_mark = models.FloatField()


class Instructions(models.Model):
    exam_id = models.OneToOneField(Exam,on_delete=models.CASCADE,null=True)
    instructions = HTMLField()

    class Meta:
        db_table = 'instructions'


class Questions(models.Model):
    exam_id  = models.ForeignKey(Exam,on_delete=models.PROTECT)
    question = models.CharField(max_length=9000)
    type = models.CharField(max_length=50)
    option = models.CharField(max_length=5000,blank=True)
    mark = models.FloatField()

    class Meta:
        db_table = 'questions'
    