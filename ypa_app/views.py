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
    context = {
        'title': 'Events',
    }
    return render(request, 'events.html', context)


def events_psb(request):
    context = {
        'title': 'Physics Speed Bowl (PSB)',
    }
    return render(request, 'events_details/psb.html', context)


def events_codeify(request):
    context = {
        'title': 'Code-ify Physics! 2020',
    }
    return render(request, 'events_details/codeify.html', context)


def events_think(request):
    context = {
        'title': 'Think Physics! 2020',
    }
    return render(request, 'events_details/think.html', context)
