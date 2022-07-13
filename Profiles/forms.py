from email.policy import default
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from Profiles.models import Customer

class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email','password') 
       
class RegisterCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name','number','address')
