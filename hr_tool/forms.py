from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from .models import Employee
from django import forms
from django.forms.widgets import PasswordInput

from django.contrib.auth import get_user_model
User = get_user_model()


# class EmployeeRegistrationForm(forms.Form):
#     username = forms.CharField(required=True)
#     email = forms.CharField(required=True)
#     password1 = forms.CharField(required=True,widget=PasswordInput)
#     password2 = forms.CharField(required=True,widget=PasswordInput)
#     position = forms.CharField(required=True)
#     department = forms.CharField(required=True)


    
class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['last_login','date_joined','groups','user_permissions']

    
class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['last_login','date_joined','password','is_superuser','is_staff','groups','user_permissions']
