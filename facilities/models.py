from django.db import models

class Facilities(models.Model):
    facility_name = models.CharField(max_length=40)
    facility_email = models.EmailField()
    phone_number = models.IntegerField()

    # Foreign Key
    hood_id = models.ForeignKey('users.Hood', on_delete=models.CASCADE)