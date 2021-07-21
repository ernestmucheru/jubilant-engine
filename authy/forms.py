from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
# from.models import Rating

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
# class RateForm(forms.ModelForm):
#     class Meta:
#         model = Rating
#         fields=['design','content','usability']