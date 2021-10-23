from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import CustomerUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomerUser
        fields = UserCreationForm.Meta.fields+('email','address','age','universitet')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomerUser
        fields = UserChangeForm.Meta.fields

