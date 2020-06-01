from django.shortcuts import render
from .forms import IssueReportForm
from django.http import HttpResponseRedirect
from django.contrib import messages


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

    return render(request, 'contact/contact.html', context)
