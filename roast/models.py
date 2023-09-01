from django.db import models
#from tiny.models import HTMLFields
class news(models.Model):
    title=models.CharField(max_length=100)
    #desc=HTMLField()
# Create your models here.