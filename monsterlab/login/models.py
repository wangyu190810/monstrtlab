#coding:utf-8
from django.db import models

# Create your models here.
class FindPassword(models.Model):
    username=models.CharField(max_length=20)
    activetion_key=models.CharField(max_length=20)
    data=models.DateField(auto_now_add=True)


