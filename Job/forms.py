from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class jobRecordForm(ModelForm):
    class Meta:
        model = Avaliable_jobs
        fields ='__all__'