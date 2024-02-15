from django.db import models
import datetime
import uuid

# Create your models here.

class TodoList(models.Model):
    taskid=models.UUIDField(auto_created=True, primary_key=True,default=uuid.uuid4)
    taskTitle=models.TextField(max_length=255,blank=False)
    taskDesc=models.TextField(null=True)
    taskCreated=models.DateTimeField(default=datetime.datetime.now())
    taskComp=models.DateTimeField(blank=True,null=True)
    
# def __str__(self):
#     return self.taskTitle[:50]
