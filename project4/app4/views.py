from django.shortcuts import render,redirect
from . forms import UserForm , UserProfileInfoForm
from django.contrib.auth import authenticate,login
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request,'app4/index.html')

def register(request):
    registerd=False
    if request.method == 'POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)
        if user_form.is_valid and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            if'profile_pic' in request.FILES:
                profile.prfile_pic=request.FILES['profile_pic']
                profile.save()
                registerd=True

    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render(request,'app4/register.html',{'user_form':user_form,
                                                'profile_form':profile_form,
                                                'registered':registerd})



def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('app4:index')
        else:
            messages.info(request,'username and password are incorrect')
    context={}
    return render(request,'app4/login.html',context)