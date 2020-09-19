from django.db import models
from django.conf import settings


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.CharField(max_length=255)

    # def __str__(self):
    #     return self.title
