from django.db import models
import datetime

from adminapp.models import Exam, Student

# Create your models here.

class ExamStatus(models.Model):
    # status_choices = (('Attended','Attended'),('Not Attended','Not Attended'))
    exam_id = models.OneToOneField(Exam,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    status = models.CharField(max_length=30)
    Attended_time = models.TimeField(default=datetime.date.today)
