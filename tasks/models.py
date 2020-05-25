from django.db import models
from datetime import datetime
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    comment = models.TextField()
    created = models.DateField()
    shifts = models.CharField(max_length=20)
    assignedBy = models.CharField(max_length=30)
    assignedTo = models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    def __str__(self):
        return  self.title




