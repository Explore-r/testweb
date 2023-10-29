# from django.shortcuts import render
# from django.shortcuts import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from .models import*
# from .forms import OrderForm
# from .forms import Orderfilter

def home(request):
    return render(request,'accounts/dashboard.html')

def products(request):
    return render(request,'accounts/products.html')

def customer(request):
    return render(request,'accounts/customer.html')

# Create your views here. 
def register(request):
    form=UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
    context={'form':form}

    if form.is_valid():
        form.save()
    return render(request,'register.html',context)

def login(request):
    form=UserCreationForm()
    context={'form':form}
    return render(request,'accounts/login.html',context)
