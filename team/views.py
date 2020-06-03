from django.shortcuts import render, get_object_or_404
from home.models import Image


def team(request):
    SidJhaImage = get_object_or_404(Image, title="Sid Jha Profile Image")
    JerryLiImage = get_object_or_404(Image, title="Jerry Li Profile Image")
    JoshuaScripcaruImage = get_object_or_404(
        Image, title="Joshua Scripcaru Profile Image")

    context = {
        'title': 'Team',
        'SidJhaImage': SidJhaImage,
        'JerryLiImage': JerryLiImage,
        'JoshuaScripcaruImage': JoshuaScripcaruImage,
    }

    return render(request, 'team/team.html', context)
