from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import date

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)
    completed_by = models.ManyToManyField(User, default=None, blank=True)
    created_on = models.DateField(default=date.today)
    
    def __str__(self):
        return self.title