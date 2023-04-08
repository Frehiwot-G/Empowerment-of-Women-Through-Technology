from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from django.template import loader
from women_in_tech import models as w_model
from Job import models as J_model
from .forms import *

# def home(request):
#     return render(request, 'AUTH/home.html')

@login_required(login_url="auth/login/")
def index(request):
    book=w_model.Traning_module.objects.all()
    mentor=w_model.Mentor.objects.all()
    care_giver=Care_giver.objects.all()
    job=J_model.Avaliable_jobs.objects.all()
   
    book_count=book.count()
    mentor_count=mentor.count()
    care_count=care_giver.count()
    job_count=job.count()
    
    context = {'segment': 'index','book_count':book_count,'mentor_count':mentor_count,'care_count':care_count,'job_count':job_count}

    html_template = loader.get_template('AUTH/index.html')
    return HttpResponse(html_template.render(context, request))

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                # return redirect("home")
                return redirect("index")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "AUTH/login.html", {"form": form, "msg": msg})


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

def logoutuser(request):
    logout(request)
    return redirect('login')




