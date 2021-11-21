from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm
from .models import User
# Create your views here.

def index(request):
    pass

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                            name = request.POST['name'],
                            nickname = request.POST['nickname'],
                            email = request.POST['email'],
                            phone_number = request.POST['phone_number'],)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'Login/signup.html')
    else:
        form = UserCreationForm
        return render(request, 'Login/signup.html', {'form':form})
