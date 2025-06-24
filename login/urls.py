from django.urls import path,include 
from . import views




urlpatterns = [
    
    path('signup.html',views.registration,name="sign_up"),
    path('',include("home.urls")),
    path('login_user',views.login_user,name="login_user"),
    path('login',views.home,name="login"),
    path('leave_form',views.leave_form,name="leave_form"),#leave form application 
    path("home",views.logged,name="logged"),#when user login the page will render without login button
    path("form_submission",views.leave_application_view,name="form_submission"),#api
    path("student_dash",views.student_dashboard,name="student_dash"),
    path("leave_planner",views.leave_planner,name="leave_planner"),
    path("warden",views.warden_dashboard,name="warden"),
    path("warden_approvals",views.warden_approvals,name= "warden_approvals")
    
    
]