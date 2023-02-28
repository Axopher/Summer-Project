from lib2to3.pgen2.token import AMPER
from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePageView,name='home'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('checkout/<str:pk>/',views.checkout,name='checkout'),
    path('process_order/',views.processOrder,name="update_item"),

]