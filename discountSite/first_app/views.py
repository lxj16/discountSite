from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request , 'first_app/index.html')

def login(request):
    return render(request, 'first_app/login.html')

def signup(request):
    return render(request, 'first_app/signUp.html')

def forgotPassword(request):
    return render(request, 'first_app/forgorPassword.html')
