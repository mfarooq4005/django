from django.db import models

class Result(models.Model):
    maths = models.IntegerField()
    eng = models.IntegerField()
    urdu = models.IntegerField()
    biy = models.IntegerField()
    phy = models.IntegerField()
    chy = models.IntegerField()
    ist = models.IntegerField()
    ps = models.IntegerField()
    total_numbers = models.CharField(max_length=25,default=None)
    percentage = models.CharField(max_length=25,default=None)
    division = models.CharField(max_length=25,default=None)
    image_selection=models.FileField(upload_to='board/', max_length=2200,default=None,null=True)