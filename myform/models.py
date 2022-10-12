from django.db import models

# Create your models here..
class student(models.Model):
    empid=models.IntegerField()
    empname=models.CharField(max_length=30)
    empage=models.IntegerField()
    empsalary=models.IntegerField()
