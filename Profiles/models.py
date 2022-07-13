import email
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self) :
        return self.name



def isAdmin(username):
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        return user.is_superuser
    else:
        return None

def getNormalUsers():
    if User.objects.filter(is_superuser=False).exists():
        users = User.objects.filter(is_superuser=False)
        return users
    else:
        return None


def getFullDetails(user,id):
    if user == 'Customer':
        if Customer.objects.filter(id=id).exists():
            return Customer.objects.get(id=id)
    
    elif user == 'User':
        if User.objects.filter(id=id).exists():
            return User.objects.get(id=id)

    return None