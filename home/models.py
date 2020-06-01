from django.db import models


class Image(models.Model):
    title = models.CharField(null=True, max_length=100)
    description = models.TextField(max_length=1000, blank=True)

    image_file = models.ImageField(null=True, upload_to='images')
    created_on = models.DateTimeField(
        null=True, auto_now_add=True, db_index=True)
