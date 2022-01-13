from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name=models.CharField(max_length=10000)
    res_type=models.CharField(max_length=10000)
    description=models.CharField(max_length=10000)
    hours=models.JSONField()

    
