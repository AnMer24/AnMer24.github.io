from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForm

# Create your views here.
def register_view(request):
    if request.method!='POST':
        form=UserCreationForm()
    else:
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password)
            login(request,user)
            
        else: return HttpResponseRedirect(reverse('index'))
    return render(request,'Users/register.html',{'form':form})

def login_view(request):
    if request.method!='POST':
        form=LoginForm()
    else:
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else: return HttpResponseRedirect(reverse('index'))
    return render(request,'Users/login.html',{'form':form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
