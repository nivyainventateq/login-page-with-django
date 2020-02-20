from django.db import models

# Create your models here.

class Logintb(models.Model):
    uname=models.CharField(max_length=50,blank=True, null=True)
    pwd=models.CharField(max_length=50,blank=True, null=True)
