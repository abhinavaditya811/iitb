from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title= models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
