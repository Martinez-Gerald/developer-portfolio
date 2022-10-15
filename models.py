from operator import truediv
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description= models.CharField(max_length=100)
    technology= models.CharField(max_length=100)
    image= models.ImageField(upload_to='gallery')
    link= models.URLField(max_length=200,null=True)
