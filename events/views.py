from django.shortcuts import render, get_object_or_404
from home.models import Image


def events(request):
    PhysicsSpeedBowlImage = get_object_or_404(
        Image, title="Home Information Image")

    context = {
        'PhysicsSpeedBowlImage': PhysicsSpeedBowlImage
    }

    return render(request, 'events/events.html', context)
