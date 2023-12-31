from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserCreationForms(UserCreationForm):
    username = forms.CharField(label='الاسم')
    firstname = forms.CharField(label='الاسم الأول')
    lastname = forms.CharField(label='الاسم الأخير')
    email = forms.EmailField(label='البريد الالكتروني')
    password1 = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(label='تأكيد كلمة المرور', widget=forms.PasswordInput(), min_length=8)

    class Meta:
        model = User
        fields = ('username', 'firstname', 'lastname', 'email', 'password1', 'password2')

                                       

class LogIn_form(forms.ModelForm):
    username = forms.CharField(label='الاسم')
    password = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'first_name': 'الاسم الأول',
            'last_name': 'الاسم الأخير',
            'email': 'البريد الالكتروني',
        }




class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'subtitle', 'address' , 'address_detail' , 'number_phone' , 'working_hours' , 'waiting_time' , 'who_i' , 'price' , 'facebook' , 'twitter' , 'google' , 'specialist_doctor' , 'tye_of_person' , 'doctor')
