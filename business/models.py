from django.db import models
from users.models import Hood

class Business(models.Model):
    business_name = models.CharField(max_length=40)
    business_email = models.EmailField()