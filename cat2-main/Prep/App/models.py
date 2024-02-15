from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class New_User(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    reg_no=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
