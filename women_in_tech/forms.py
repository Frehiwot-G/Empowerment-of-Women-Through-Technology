from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class bookRecordForm(ModelForm):
    class Meta:
        model = Traning_module
        fields ='__all__'
        
class skillRecordForm(ModelForm):
    class Meta:
        model = Technological_skills
        fields ='__all__'

class mentorRegisterForm(ModelForm):
    class Meta:
        model = Mentor
        fields ='__all__'