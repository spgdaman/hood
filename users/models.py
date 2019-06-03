from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Users(AbstractUser):
    pass

class Profile(models.Model):
    bio = models.CharField(max_length=160)
    location = models.CharField(max_length=40)

    #Foreign Key
    user_id = models.OneToOneField(Users, on_delete=models.CASCADE)

class Hood(models.Model):
    hood_name = models.CharField(max_length=40)
    hood_location = models.CharField(max_length=40)
    occupant_count = models.IntegerField()

    @classmethod
    def create_hood(cls,name,location,count):
        hood = cls.objects.create(hood_name=name,hood_location=location,occupant_count=count)
        return hood
    
    @classmethod
    def delete_hood(cls,hood_id):
        cls.objects.filter(id=hood_id).delete()
        return True
    
    @classmethod
    def find_hood(cls,hood_id):
        hoods = cls.objects.filter(id__icontains=hood_id)
        return hoods

    @classmethod
    def update_hood(cls,new_name):
        hood = cls.objects.update(hood_name=new_name)
        return hood

    @classmethod
    def update_occupants(cls,new_count):
        hood = cls.objects.update(occupant_count=new_count)
        return hood