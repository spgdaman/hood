from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import NewHood,UsersCreationForm
from django.contrib.auth import login,authenticate

def home(request):
    return render(request,'index.html')

def new_hood(request):
    # current_user = request.current_user
    if request.method == 'POST':
        form = NewHood(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # post.user = current_user
            post.save()
        return redirect('home')
    else:
        form = NewHood()
    return render(request,'newhood.html',{'form':form})

def register(request):
    if request.method == 'POST':
        form = UsersCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UsersCreationForm()
        return render(request, 'auth/register.html', {'form': form})

            