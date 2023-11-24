from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def home(request):
    return render(request, 'plan/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'plan/signupuser.html', {'form': CustomUserCreationForm})
    else:
        # Create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentplan')
            except IntegrityError:
                return render(request, 'plan/signupuser.html', {'form': CustomUserCreationForm,
                                                                'error_username': 'This username has already been taken! Please choose a new username!'})
        else:
            return render(request, 'plan/signupuser.html',
                          {'form': CustomUserCreationForm, 'error_password': 'Passwords did not match'})
        # Tell the user the passwords didn't match


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'plan/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is None:
            return render(request, 'plan/loginuser.html',
                          {'form': AuthenticationForm(), 'errorUA': 'USERNAME AND PASSWORD DID NOT MUTCH'})
        else:
            login(request, user)
            return redirect('currentplan')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def currentplan(request):
    return render(request, 'plan/currentplan.html')
