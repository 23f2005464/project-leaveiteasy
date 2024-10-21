from django.urls import path,include 
from . import views




urlpatterns = [
    path('',views.home,name="login"),
    path('signup.html',views.registration,name="sign_up"),
    path('home',include("home.urls")),
    path('login_user',views.login_user,name="login_user"),
    path('login',views.home,name="login")
    
]