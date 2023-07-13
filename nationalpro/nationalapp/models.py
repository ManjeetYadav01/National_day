from operator import mod
from django.db import models

# Create your models here.

class Calender(models.Model):
    month=models.CharField(max_length=20,blank=False,null=False)
    date=models.IntegerField()
