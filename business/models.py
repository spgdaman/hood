from django.db import models
from users.models import Hood

class Business(models.Model):
    business_name = models.CharField(max_length=40)
    business_email = models.EmailField()

    @classmethod
    def create_business(cls,name,email):
        business = Business.objects.create(business_name=name,business_email=email)
        return business

    @classmethod
    def delete_business(cls,business_id):
        Business.objects.filter(id=business_id).delete()
        return True

    @classmethod
    def find_business(cls,business_name):
        businesses = Business.objects.filter(business_name__icontains=business_name)
        return businesses