from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserCreationForms(UserCreationForm):
    username = forms.CharField(label='الاسم')
    firstname = forms.CharField(label='الاسم الأول')
    lastname = forms.CharField(label='الاسم الأخير')
    email = forms.EmailField(label='البريد الالكتروني')
    password1 = forms.EmailField(label='كلمة المرور', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.EmailField(label='تأكيد كلمة المرور', widget=forms.PasswordInput(), min_length=8)

    class Meta:
        model = User
        fields = ('username','firstname','lastname','email','password1','password2')
                                       



class LogIn_form(forms.ModelForm):
    username = forms.CharField(label='الاسم')
    password = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')
