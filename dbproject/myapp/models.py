from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100) # A field for storing names as text
    status = models.CharField(max_length=100) # A field for storing status as text