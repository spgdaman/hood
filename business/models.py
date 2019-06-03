from django.db import models
from users.models import Hood

class Business(models.Model):
    business_name = models.CharField(max_length=40)
    business_email = models.EmailField()

    @classmethod
    def create_business(cls,name,email):
        business = cls.objects.create(business_name=name,business_email=email)
        return business

    @classmethod
    def delete_business(cls,business_id):
        cls.objects.filter(id=business_id).delete()
        return True

    @classmethod
    def find_business(cls,business_name):
        businesses = cls.objects.filter(business_name__icontains=business_name)
        return businesses
    
    @classmethod
    def update_business(cls,business_name,new_name):
        business = cls.objects.filter(business_name=business_name).update(business_name=new_name)
        return business