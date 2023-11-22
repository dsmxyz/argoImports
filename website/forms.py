from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    username=forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    email=forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))

    class Meta:
        model=User
        fields=('username', 'email', 'password1', 'password2')
        