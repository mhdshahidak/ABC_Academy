from django.db import models
from adminapp.models import Student
# Create your models here.

class Payment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.PROTECT)
    paidamount = models.IntegerField(default=0)
    paiddate = models.DateField()

    class Meta:
        db_table='payment'