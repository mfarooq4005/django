from django.db import models
class titles(models.Model):
    main_title=models.CharField(max_length=16)
    main_description=models.CharField(max_length=200)
# Create your models here.
