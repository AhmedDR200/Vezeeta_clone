from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def doctors_list(request):
    doctors = User.objects.all()

    return render(request, 'user/doctors_list.html', {'doctors':doctors})