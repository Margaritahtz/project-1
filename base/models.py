from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass
    

    




    #username = models.CharField(max_length=200, null=True, unique=True)
    #email = models.EmailField(unique=True, null=True)

    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = []

#avatar = models.ImageField(null=True, default="avatar.svg")
    

class data(models.Model):
    Datestamp = models.CharField(max_length=200)
    Timestamp = models.CharField(max_length=200)
    TopTemperature = models.FloatField(null=True)
    #FeedTemperature = 

def __init__(self, TopTemperature):
    return self.TopTemperature



