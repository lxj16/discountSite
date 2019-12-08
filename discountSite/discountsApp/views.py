from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from . import views
from . import forms
from .models import User

# Create your views here.


def main_page(request):
    return render(request, 'discountsApp/mainPage.html')


def index(request):
    return render(request, 'discountsApp/index.html')


def login(request):
    return render(request, 'discountsApp/login.html')


def signup(request):

    form = forms.signUpForm()
    if request == 'POST':
        form = forms.signUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('user_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            new_user = User(name=username, password=password, email=email)
            new_user.save()
            return redirect('home')
        else:
            form = forms.signUpForm()
    return render(request, 'discountsApp/signUp.html', {'form': form})


def forgotPassword(request):
    return render(request, 'discountsApp/forgorPassword.html')
