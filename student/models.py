from django.db import models
import datetime

from adminapp.models import Exam, Student,Questions

# Create your models here.

class ExamStatus(models.Model):
    # status_choices = (('Attended','Attended'),('Not Attended','Not Attended'))
    exam_id = models.ForeignKey(Exam,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    status = models.CharField(max_length=30)
    Attended_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('exam_id', 'student')

class Answer(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE,null=True)
    question = models.ForeignKey(Questions,on_delete=models.CASCADE,null=True)
    savedaswer=models.CharField(max_length=30000)
    ans_true = models.BooleanField(default=False)
    mark = models.FloatField(default=0)
    status=models.CharField(max_length=30,null=True)
