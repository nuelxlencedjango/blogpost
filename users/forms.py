from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class UserRegisterForm(UserCreationForm):
   # username =forms.CharField()
    email = forms.EmailField()
   # password1 =forms.PasswordInput()
    #password2 =forms.CharField()
    
    class Meta:
        model = User
        fields = ['username' ,'email' ,'password1' ,'password2']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:

        model = User
        fields = ['username' ,'email']
    

    

class ProfileUpdateForm(forms.ModelForm):
    class Meta:

        model = Profile
        fields = ['image']
    
