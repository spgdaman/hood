from django.forms import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Users,Hood

class UsersCreationForm(UserCreationForm):

    class meta:
        model = Users
        fields = ('email')

class UsersChangeForm(UserChangeForm):

    class Meta:
        model = Users
        fields = ('username', 'email')

class NewHood(Hood):
    
    class meta:
        model = Hood
        fields = ('hood_name', 'hood_location', 'occupant_count')