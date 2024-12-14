from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render(request,'admin.html')

def create_customer(request):
    customers = Customer.objects.all()
    return render(request,'create_customer.html',{'customers':customers})

def customers(request):
    return render(request,'customers.html')

