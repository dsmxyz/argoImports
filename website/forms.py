from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer

class SignUpForm(UserCreationForm):
    username=forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    email=forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))

    class Meta:
        model=User
        fields=('username', 'email', 'password1', 'password2')
        
class addCustomersForm(forms.ModelForm):
    name=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Customer name","class":"form-control"}), label="")
    email=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email","class":"form-control"}), label="")
    phone=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone","class":"form-control"}), label="")
    address=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address","class":"form-control"}), label="")
    city=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City","class":"form-control"}), label="")
    state=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State","class":"form-control"}), label="")
    zipcode=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode","class":"form-control"}), label="")

    class Meta:
        model=Customer
        exclude=("user",)