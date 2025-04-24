from django.shortcuts import render, redirect,HttpResponse
from .forms import SignupForm,LeaveApplicationForm
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User,Group
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.hashers import make_password,check_password






# Create your views here.
def home(request):
    print("requested")
    return render(request,"index.html")

def main_home(request):
      return render()

def logged(request):
    return render(request,"logged_user.html")

def registration(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.password = make_password(form.cleaned_data['password']) 
            user.save()
            return redirect('login')
        else:
            return render(request, 'base.html', {'form': form})   
    else:
        return render(request, 'base.html', {'form': form})   
    

def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user_type = data['role']
        
        try:
            user = Chat_signup.objects.get(username=username)
            if check_password(password, user.password) and user.role == user_type:
                # Mock login by setting session or token
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                request.session['role'] = user.role
                if user_type == 'user':
                    return JsonResponse({'success': True, 'redirect_url': '/home'})
                elif user_type == 'admin':
                    return JsonResponse({'success': True, 'redirect_url': '/admin/'})
                else:
                    return JsonResponse({'success': False, 'error': 'Invalid user type'})
            else:
                return JsonResponse({'success': False, 'error': 'Invalid credentials or user type'})
        except Chat_signup.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'User does not exist'})
               
    return render(request,'login.html')             


#****api****
def leave_form(request):
    return render(request,"form.html")

def leave_application_view(request):
    if request.method == 'POST':
        form = LeaveApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # replace with your URL name
    else:
        form = LeaveApplicationForm()
    return render(request, 'form.html', {'form': form})