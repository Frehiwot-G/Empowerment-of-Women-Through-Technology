from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email address",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

class CaregiversRegistrationForm(ModelForm):
    class Meta:
        model = Care_giver
        fields ='__all__'
        
