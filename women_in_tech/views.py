from django.shortcuts import redirect, render
from .models import *
from .forms import *
# Create your views here.

def record_book(request):
    if request.method == 'POST':
        form = bookRecordForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('login')
            return redirect('record_book')
            # return render(request, 'admin/record_book.html')
    else:
        form = bookRecordForm()

    context = {'form': form}
    return render(request, 'admin/record_book.html', context)


def record_skills(request):
    if request.method == 'POST':
        form = skillRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record_skills')
            # return render(request, 'admin/record_skills.html')
    else:
        form = skillRecordForm()

    context = {'form': form}
    return render(request, 'admin/record_skills.html', context)

def register_mentor(request):
    if request.method == 'POST':
        form = mentorRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('login')
            return redirect('register_mentor')
            # return render(request, 'admin/record_book.html')
    else:
        form = mentorRegisterForm()

    context = {'form': form}
    return render(request, 'admin/register_mentor.html', context)


def modulePage(request):
    modules=Traning_module.objects.all()
    return render(request, 'women_in_tech/module.html',{'modules':modules})

def mentorsPage(request):
    mentors=Mentor.objects.all()
    return render(request, 'women_in_tech/mentors.html',{'mentors':mentors})