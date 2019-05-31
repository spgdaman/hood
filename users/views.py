from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import NewHood

def home(request):
    return render(request,'index.html')

def new_hood(request):
    current_user = request.current_user
    if request.method == 'POST':
        form = NewHood(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('home')
    else:
        form = NewHood()
    return render(request,'newhood.html',{'form':form})