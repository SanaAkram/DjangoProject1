from django.shortcuts import render
from .models import Profiles


# Create your views here.


def profiles(request):
    profiles = Profiles.objects.all()
    context = {'profiles': profiles}
    return render(request, "users/profiles.html", context)


def userProfile(request, pk):
    profile = Profiles.objects.get(pk=pk)
    context = {'profile': profile}
    return render(request, 'users/user-profile.html', context)
