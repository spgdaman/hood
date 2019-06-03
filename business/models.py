from django.db import models
from users.models import Hood

class Business(models.Model):
    business_name = models.CharField(max_length=40)
    business_email = models.EmailField()

    @classmethod
    def create_business(cls,name,email):
        business = Business.objects.create(business_name=name,business_email=email)
        return business

    