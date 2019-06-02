from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Facilities

@login_required(login_url='/accounts/login/')
def facilities(request):
    facilities = Facilities.objects.all()
    return render(request,'facilities.html',{"facilities":facilities})

@login_required(login_url='/accounts/login/')
def facility_search(request):
    current_user = request.user
    if 'facility' in request.GET and request.GET['facility']:
        search_term = request.GET.get('facility')
        search_item = Facilities.objects.filter(facility_name__icontains = search_term)
        message=f"{{search_term}}"
        return render(request,'facilitysearch.html',{"message":message,"facilities":search_item})
    else:
        message = "Please enter a correct search term"
        return render(request,"facilitysearch.html")

@login_required(login_url='/accounts/login/')
def facility(request,facility_id):
    facility = Facilities.objects.filter(id=facility_id)
    return render(request,'facility.html',{"facility":facility})