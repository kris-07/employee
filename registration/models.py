from django.db import models
from datetime import datetime

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    bio = models.CharField(max_length=500)
    username = models.CharField(max_length=20)
    img = models.ImageField(upload_to='pics')
    countrycode = models.CharField(max_length=5)
    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=500)
    pincode = models.IntegerField(default=0)
    gender = models.CharField(max_length=10)
    dob=models.DateTimeField(default=datetime(1900,1,1))
    
