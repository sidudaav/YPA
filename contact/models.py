from django.db import models


class IssueReport(models.Model):
    title = models.CharField(null=True, max_length=1000)
    description = models.TextField(null=True, max_length=2000)

    created_on = models.DateTimeField(null=True, auto_now_add=True)
