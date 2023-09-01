from django.db import models
class titles(models.Model):
    main_title=models.CharField(max_length=20)
    main_description=models.CharField(max_length=200)
    image_url = models.CharField(default='default_image_url',max_length=1200)
# Create your models here.
