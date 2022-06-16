from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePageView,name='home'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerUser,name='register'),
    # path('usersPage/',views.usersPage,name='usersPage'),
]