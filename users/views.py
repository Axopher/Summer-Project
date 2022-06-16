from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib import messages

from .forms import ProfileForm

from django.contrib.auth.forms import UserCreationForm

from django.db.models.signals import post_save
from .models import Profile
from adminpanel.models import Student
# Create your views here.

def HomePageView(request):
    return render(request,'users/home.html')

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

def registerUser(request):
    page = 'register'
    form = ProfileForm()

    if request.method == 'POST':
        form1 = ProfileForm(request.POST)
        # form2 = UserCreationForm(request.POST)
        if form1.is_valid():
            user = form1.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,'Your profile is created!')

        # if form2.is_valid():
        #     user = form2.save(commit=False)
        #     user.username = user.username.lower()
        #     user.password = user.username.lower()
        #     user.save()
        #     print(user)
        #     messages.success(request,'Your account is created and your password is same as your username, change it.')
        #     login(request,user)
        #     return redirect('dashboard')


    context = {'page':page,'form':form}
    return render(request,'users/login_register.html',context)

# def UserCreated(sender,instance,created,**kwargs):
#     if created:
#         profile = instance
#         user = User.objects.create(
#             user = user,
#             username = profile.username,
#             password1 = profile.username,
#             password2 = profile.username

#         )

    


# post_save.connect(UserCreated,sender=Profile)
# def usersPage(request):
#     return render(request,'users/userPage.html')