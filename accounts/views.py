from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import LogIn_form , UserCreationForms , UpdateUserForm
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required
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
          user =authenticate (request, username=username, password=password )
          if user is not None:
               login(request, user)
               return redirect('accounts:doctors_list')
          else:
               form=LogIn_form()     
     form = LogIn_form()
     return render(request, 'user/login.html', {'form':form})





def signup(request):
     form = UserCreationForms()
     if request.method == 'POST':
          form = UserCreationForms(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               password = form.cleaned_data.get('username')
               user =authenticate (username=username, password=password )
               login(request, user)
               return redirect('accounts:doctors_list')

     else: 
          form = UserCreationForms()
               
     return render(request, 'user/signup.html', {'form':form})



@login_required(login_url='accounts:login')
def myprofile(request):
     return render(request, 'user/myprofile.html', {})



def update_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('accounts:doctors_list')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'user/update_profile.html', {'user_form': user_form})