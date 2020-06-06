from django.shortcuts import render, get_object_or_404
from .models import Image


def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'home/home.html', context)
