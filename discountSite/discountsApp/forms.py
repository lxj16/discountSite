from django import forms
from django.core import validators
from . import models


class signUpForm(forms.Form):
    user_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ('name', 'email', 'password', 'country')
