import re
from django.shortcuts import render,redirect
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import UpdateProfileForm
from .models import Profile

import logging
logger=logging.getLogger('django')


# Create your views here.

# ========================================== auth part =======================================================

def registration_validation(request,password):
    error=[]
    if not re.search(r'[A-Z]',password):
        error.append('Your password should contain at list one capital letter')
    if not re.search(r'\d',password):
        error.append('Your password should contain at list one degits')
    if not re.search(r'[!@#$%^&*<>]',password):
        error.append('Your password should contain at least one specific symbol')    
    return error

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exists')
                return redirect("register")

            if User.objects.filter(email=email).exists():
                messages.error(request,'Email already exists')
            
            message_error=registration_validation(request,password=password)
            messages.error(request,message_error)

            if not message_error:
                User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                messages.success(request,f'Hello {first_name} Your account is been successfully register')
                return redirect('log_in')
            else:
                messages.error(request,"Your password doesnot match")
                return redirect('register')

    return render(request,'accounts/register.html')


def log_in(request):
    try:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']

            if not User.objects.filter(username=username).exists():
                messages.error(request,'Username does not exists')
                return redirect('log_in')
            user=authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.error(request,'Your password is incorrect')
                return redirect('log_in')
    except Exception as e:
        logger.error(str(e),exc_info=True)

    return render(request,'accounts/login.html')

def log_out(request):
    logout(request)
    return redirect('log_in')

def change_password(request):
    form=PasswordChangeForm(user=request.user)
    if request.method =='POST':
        form=PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
    return render(request,'accounts/changepass.html',{'form':form})

    
    subject="Dream Success"
    message="hello"
    from_email='prajapatibishal57@gmail.com'
    reciption_list=["email"]
    send_mail(subject,message,from_email,reciption_list,fail_silently=False)

# ====================================================================================================================
# ================================ profile ======================================================================
@login_required(login_url='log_in')
def profile_base(request):
    return render(request,'profile/profile_base.html')
    
@login_required(login_url='log_in')
def profile(request):
    return render(request,'profile/profile.html')

@login_required(login_url='log_in')
def update_profile(request):
    profile,created=Profile.objects.get_or_create(user=request.user)
    form=UpdateProfileForm(instance=profile)
    
    if request.method=='POST':
        form=UpdateProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context={
        'form':form,
        'user':request.user,
        'profile':request.user.profile
    }
    return render(request,'profile/upload_profile.html',context)
