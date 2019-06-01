from django.forms import forms
from .models import Users,Hood
from django.contrib.auth.forms import UserCreationForm

class NewHood(Hood):
    
    class meta:
        model = Hood
        fields = ('hood_name', 'hood_location', 'occupant_count')

class UserForm(UserCreationForm):

    class meta:
        model = Users
        fields = ('username', 'email')