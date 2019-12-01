from django.shortcuts import render
from django.http import HttpResponse
from . import views
from . import forms

# Create your views here.
def index(request):
    return render(request , 'first_app/index.html')

def login(request):
    return render(request, 'first_app/login.html')

def signup(request):
    form = forms.signUpForm
    return render(request, 'first_app/signUp.html',{'form' : form})

def forgotPassword(request):
    return render(request, 'first_app/forgorPassword.html')
