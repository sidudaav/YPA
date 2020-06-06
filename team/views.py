from django.shortcuts import render, get_object_or_404
from home.models import Image


def team(request):
    context = {
        'title': 'Team',
    }

    return render(request, 'team/team.html', context)
