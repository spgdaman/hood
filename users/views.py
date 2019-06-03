from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import NewHood,UserForm
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Hood
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def home(request):
    hoods = Hood.objects.all()
    return render(request,'index.html',{"hoods":hoods})

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('home')
    else:
        form = UserForm()
        return render(request, 'auth/register.html', {'form': form})

            