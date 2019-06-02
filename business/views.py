from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Business

@login_required(login_url='/accounts/login/')
def businesses(request):
    businesses = Business.objects.all()
    return render(request,'businesses.html',{"businesses":businesses})
