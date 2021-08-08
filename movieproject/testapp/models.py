from django.db import models

# Create your models here.
class Movie(models.Model):
    rdate=models.DateField()
    moviename=models.CharField(max_length=30)
    hero=models.CharField(max_length=200)
    heroine=models.CharField(max_length=200)
    rating=models.IntegerField() 
    platform=models.CharField(max_length=100)