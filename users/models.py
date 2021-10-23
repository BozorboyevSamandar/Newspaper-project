from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomerUser(AbstractUser):
    age = models.PositiveIntegerField(null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    universitet = models.CharField(max_length=200,null=True,blank=True)
