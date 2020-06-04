from django.shortcuts import render, get_object_or_404


def home(request):
    context = {
        'title': 'Chapters'
    }
    return render(request, 'chapters/home.html', context)


def view_chapters(request):
    context = {
        'title': 'Chapters'
    }
    return render(request, 'chapters/view_chapters.html', context)
