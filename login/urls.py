from django.urls import path,include 
from . import views




urlpatterns = [
    
    path('signup.html',views.registration,name="sign_up"),
    path('',include("home.urls")),
    path('login_user',views.login_user,name="login_user"),
    path('login',views.home,name="login"),
    path('leave_form',views.leave_form,name="leave_form"),
    path("home",views.logged,name="logged"),
    path("form_submission",views.leave_application_view,name="form_submission")
]