from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from Profiles.forms import RegisterCustomerForm, RegisterUserForm
from .models import Customer, getFullDetails, getNormalUsers, isAdmin

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        name = request.session['username']
        data = {
                    'username' : name,
                    'is_superuser' : isAdmin(name) 
                }
        if isAdmin(name):
            customers = Customer.objects.all()
            nusers = getNormalUsers()
            extraData = {
                'customers':customers,
                'users':nusers
            } 
            data.update(extraData)
        else:
            customers = Customer.objects.all()
            extraData = {
                'customers':customers,
            } 
            data.update(extraData)
                
        return render(request,'userContent.html',context=data)
    else:
        return redirect('login')

def signin(request):
    if request.method == "POST":
        name = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=name, password=pwd)
        if user is not None:
            # A backend authenticated the credentials
            request.session['username'] = name
            return redirect('home')
        else:
            # No backend authenticated the credentials
            print("NOT Valid CREDs")

    return render(request,'dash.html',{'alert':None})

def registerSuperUser(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.instance.is_staff = True
            form.instance.is_superuser = True
            user = form.save()
            password = form.cleaned_data['password']

            #  Use set_password here
            user.set_password(password)
            user.save()

            # return render(request,'dash.html',{'alert':'success'})
            return redirect('login')
        else:
            return HttpResponse(form.errors)
    form = RegisterUserForm()
    return render(request,'register.html',{'form':form})

def logout(request):
    try:
        del request.session['username']
    except:
        return redirect('login')
    return redirect('login')

def createUser(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'userForm.html',{'form':form,'alert':'success','userType':'User'})

    form = RegisterUserForm()
    return render(request,'userForm.html',{'form':form,'userType':'User'})

def createCustomer(request):
    if request.method == "POST":
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'userForm.html',{'form':form,'alert':'success','userType':'Customer'})

    form = RegisterCustomerForm()
    return render(request,'userForm.html',{'form':form,'userType':'Customer'})

def getDetails(request,pk=None):
    if request.user.is_authenticated:
        cid = pk
        name = request.session['username']
        print(cid)
        userType = str(request.path)
        if 'user' in userType:
            print("CHECK IN USER TABLE")
            user = getFullDetails('User',cid)
            data ={ 
                'username':user.username,
                'email':user.email,
            }
            return render(request,'detail.html',{'data':data,'userType':'User'})
        else:
            print("CHECK IN CUSTOMER TABLE")
            cust = getFullDetails('Customer',cid)
            data ={ 
                'name':cust.name,
                'number':cust.number,
                'address':cust.address
            }
            return render(request,'detail.html',{'data':data,'userType':'Customer'})
        