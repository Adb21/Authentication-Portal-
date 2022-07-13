from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin,name='login'),
    path('register', views.registerSuperUser,name='registerSuperUser'),
    path('logout', views.logout, name='logout'),
    path('createUser', views.createUser, name='createUser'),
    path('createCustomer', views.createCustomer, name='createCustomer'),
    path('home', views.home, name='home'),
    path('user/<int:pk>', views.getDetails, name='user'),
    path('customer/<int:pk>', views.getDetails, name='customer'),
]