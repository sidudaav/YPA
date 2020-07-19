from django.contrib import admin
from .models import IssueReport


class IssueReportAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_on']


admin.site.register(IssueReport, IssueReportAdmin)