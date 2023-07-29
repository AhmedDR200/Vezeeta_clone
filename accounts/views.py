from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.


def doctors_list(request):
    doctors = User.objects.all()

    return render(request, 'user/doctors_list.html', {'doctors':doctors})



def doctors_detail(request, slug):
     doctors_detail = Profile.objects.get(slug =slug)

     return render(request, 'user/doctors_detail.html', {'doctors_detail':doctors_detail})