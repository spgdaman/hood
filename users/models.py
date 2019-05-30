from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=40)
    email = models.EmailField()

    # Foreign Key
    hood_id = models.ForeignKey(Hood, on_delete=models.CASCADE)

class Profile(models.Model):
    bio = models.CharField(max_length=160)
    location = models.CharField(max_length=40)

    #Foreign Key
    user_id = models.OneToOneField(Users, on_delete=models.CASCADE)