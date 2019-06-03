from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Business

@login_required(login_url='/accounts/login/')
def businesses(request):
    businesses = Business.objects.all()
    return render(request,'businesses.html',{"businesses":businesses})

@login_required(login_url='/accounts/login/')
def business_search(request):
    if 'business' in request.GET and request.GET['business']:
        search_term = request.GET.get('business')
        search_item = Business.objects.filter(business_name__icontains = search_term)
        message=f"{{search_term}}"
        return render(request,'businesssearch.html',{"message":message,"businesses":search_item})
    else:
        message = "Please enter a correct search term"
        return render(request,"businesssearch.html")

@login_required(login_url='/accounts/login/')
def business(request,business_id):
    business = Business.objects.filter(id=business_id)
    return render(request,'business.html',{"business":business})