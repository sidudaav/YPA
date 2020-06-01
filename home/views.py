from django.shortcuts import render, get_object_or_404
from .models import Image


def home(request):
    HomeImage = get_object_or_404(Image, title="Home Information Image")
    context = {
        'HomeImage': HomeImage
    }
    return render(request, 'home/home.html', context)
