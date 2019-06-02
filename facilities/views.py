from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Facilities

@login_required(login_url='/accounts/login/')
def facilities(request):
    facilities = Facilities.objects.all()
    return render(request,'facilities.html',{"facilities":facilities})