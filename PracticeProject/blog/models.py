from django.utils import timezone

from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.TextField(max_length=100)
    descr = models.TextField(max_length=300)
    image = models.ImageField(upload_to='blog/images')
    date_posted = models.DateTimeField(default=timezone.now)

