from .models import Image
from .forms import IssueReportForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.


def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'home.html', context)


def articles(request):
    return render(request, 'articles.html')


def sample(request):
    return render(request, 'sample.html')


def chapters_home(request):
    context = {
        'title': 'Chapters'
    }
    return render(request, 'home.html', context)


def view_chapters(request):
    context = {
        'title': 'Chapters'
    }
    return render(request, 'view_chapters.html', context)


def contact(request):
    if request.method == "POST":
        report_form = IssueReportForm(request.POST)
        if report_form.is_valid():
            report_form.save()

            messages.success(request, f'Your issue has been reported')
            return HttpResponseRedirect('/contact/')
    else:
        report_form = IssueReportForm()

    context = {
        'title': 'Contact',
        'report_form': report_form
    }

    return render(request, 'contact.html', context)


def team(request):
    context = {
        'title': 'Team',
    }

    return render(request, 'team.html', context)


def events(request):
    return render(request, 'events.html')


def events_psb(request):
    return render(request, 'events_details/psb.html')
