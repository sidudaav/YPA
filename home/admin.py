from django.contrib import admin
from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_on']


admin.site.register(Image, ImageAdmin)
