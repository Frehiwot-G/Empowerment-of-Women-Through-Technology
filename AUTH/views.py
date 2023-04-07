from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.views import View
from .forms import UserRegistrationForm,CaregiversRegistrationForm

def home(request):
    return render(request, 'home.html')

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            # return redirect('login')
            return render(request, 'AUTH/login.html')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'AUTH/register_user.html', context)

def register_care_givers(request):
    if request.method == 'POST':
        form = CaregiversRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            # return redirect('login')
            return render(request, 'AUTH/home.html')
    else:
        form = CaregiversRegistrationForm()

    context = {'form': form}
    return render(request, 'AUTH/register_caregiver.html', context)






