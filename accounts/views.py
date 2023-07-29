from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import LogIn_form
from django.contrib.auth import authenticate , login
# Create your views here.


def doctors_list(request):
    doctors = User.objects.all()

    return render(request, 'user/doctors_list.html', {'doctors':doctors})



def doctors_detail(request, slug):
     doctors_detail = Profile.objects.get(slug =slug)

     return render(request, 'user/doctors_detail.html', {'doctors_detail':doctors_detail})



def user_login(request):
     if request.method == 'POST':
          form=LogIn_form()
          username = request.POST['username']
          password = request.POST['password']
          user =authenticate (username=username, password=password )
          if user is not None:
               login(request, user)
               return redirect('accounts:doctors_list')
          else:
               form=LogIn_form()     
     form = LogIn_form()
     return render(request, 'user/login.html', {'form':form})


def myprofile(request):
     return render(request, 'user/myprofile.html', {})