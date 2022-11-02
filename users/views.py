from django.shortcuts import render
from .models import Profiles


# Create your views here.


def profiles(request):
    profiles = Profiles.objects.all()
    context = {'profiles': profiles}
    return render(request, "users/profiles.html", context)


def userProfile(request, pk):
    profile = Profiles.objects.get(pk=pk)
    topskills = profile.skill_set.exclude(description__exact="")
    otherskills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'topskills': topskills, 'otherskills': otherskills}
    return render(request, 'users/user-profile.html', context)
