from itertools import product
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib import messages

# from .forms import ProfileForm
import datetime
import re

from django.db.models.signals import post_save
from .models import *

from django.http import JsonResponse
import json
# Create your views here.

def HomePageView(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        print(search_query)

    products = Product.objects.filter(productName__icontains=search_query)


    return render(request,'users/home.html',{'products':products})

def checkout(request,pk):
    product = Product.objects.get(id=pk)
    context = {
        'product':product
    }

    return render(request,'users/checkout.html',context)

def processOrder(request):
    # transaction_id  = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    name = data['form']['name']
    phone = data['form']['phone']
    email = data['form']['email']
    address = data['form']['address']
    gender = data['form']['gender']

    

    product = Product.objects.get(id=data['productId'])

    Order.objects.create(
		product=product,
        sname=name,
        sphone=phone,
        semail=email,
        saddress=address,
        sgender=gender
		)

    return JsonResponse('Payment completed!', safe=False)


def loginUser(request):
    page = 'login'

    context = {
        'page':page
    }

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.warning(request,'user does not exist')

        user = authenticate(request,username=username,password=password)

        if user is not None:
        # login function will create a session for this user in the database in that session table
        # and also get that session and add that into our  browser's cookie
            login(request,user)
            messages.success(request,'user successfully logged in')
            return redirect('dashboard')
        else:
            messages.warning(request,'username or password is incorrect')
        

    return render(request,'users/login_register.html',context)

def logoutUser(request):
    logout(request)
    messages.success(request,'user was successfully logged out')
    return redirect('login')    

